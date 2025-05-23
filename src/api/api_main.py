import torch

from fastapi import FastAPI

from api.utils import load_checkpoint, normalize_features
from api.data_models import (
    WeatherSequence,
    ModelOutput,
)

from utils.lstm import LSTMRegressor


device = 'gpu' if torch.cuda.is_available() else 'cpu'
weather_model = load_checkpoint(
    '../resource/models/lstm_only/4layer_cp3.tar',
    LSTMRegressor(7, 5, num_layers=4, fc_hidden_dims=()),
    device=device
)
weather_model.eval()


app = FastAPI(
    version="0.1.0",
    title="Weather Prediction with LSTM API",
    summary="API for sending weather data to our model and receiving the predictions.",
    description="Visit /documentation for more information.",
    redoc_url="/documentation"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Cho phép React frontend gọi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/model_architecture/")
def get_model_architecture():
    """
    Get the current predicting model's architecture.
    """
    return {"model": str(weather_model)}

@app.post("/predict_weather/")
def predict(date_sequence: WeatherSequence) -> ModelOutput:
    """
    Predict the weather statistics of the next day given a sequence
        of weather statistics at the specified location.

    Unlike the WeatherStats, this will output unbounded results and thus,
        may be unrealistic.
    """
    in_features = torch.tensor([[
            stats.humidity, stats.pressure, stats.temperature,
            stats.wind_direction, stats.wind_speed,
        ] for stats in date_sequence
    ], dtype=torch.float32)
    city_coords = torch.tensor(date_sequence.city_coords, dtype=torch.float32)\
                       .repeat(in_features.shape[0], 1)

    with torch.no_grad():
        output = weather_model(
            torch.concat([normalize_features(in_features), city_coords], dim=1)
                 .to(device)
                 .unsqueeze(0)
        ).squeeze().cpu()

    return {
        "humidity" : output[0].item(),
        "pressure" : output[1].item(),
        "temperature" : output[2].item(),
        "wind_direction" : output[3].item(),
        "wind_speed" : output[4].item()
    }