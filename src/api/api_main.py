import torch

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.utils import (
    denormalize_features,
    load_checkpoint,
    normalize_features,
)
from api.data_models import (
    WeatherSequence,
    ModelOutput,
)

from utils.lstm import LSTMRegressor


model_configs = [
    {
        'checkpoint': '../resource/models/lstm_only/4layer_cp3.tar',
        'params': {'in_features': 7, 'out_features': 5, 'num_layers': 4, 'fc_hidden_dims': ()},
    },
    {
        'checkpoint': '../resource/models/lstm_mlp/4layer_2mlp_cp4.tar',
        'params': {'in_features': 7, 'out_features': 5, 'num_layers': 4},
    },
]
current_index = 0
device = 'gpu' if torch.cuda.is_available() else 'cpu'
weather_model = load_checkpoint(
    model_configs[current_index]['checkpoint'],
    LSTMRegressor(**model_configs[0]['params']),
    device=device
).eval()


app = FastAPI(
    version="0.1.0",
    title="Weather Prediction with LSTM API",
    summary="API for sending weather data to our model and receiving the predictions.",
    description="Visit /documentation for more information.",
    redoc_url="/documentation"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def get_root(): return {"documentation": "Documentation at /documentation."}

@app.get("/model_architecture/")
def get_model_architecture():
    """
    Get the current predicting model's architecture.
    """
    return {
        "model_index": current_index,
        "model": str(weather_model),
    }

@app.put("/set_model/{model_index}")
def set_model(model_index: int):
    global weather_model, current_index
    if model_index > len(model_configs) - 1:
        raise HTTPException(status_code=404, detail=f"Model {model_index} not found! There are only {len(model_configs)} models.")
    elif model_index < 0:
        raise HTTPException(status_code=400, detail="Cannot process negative model_index!")
    current_index = model_index
    weather_model = load_checkpoint(
        model_configs[current_index]['checkpoint'],
        LSTMRegressor(**model_configs[current_index]['params']),
        device=device
    ).eval()
    return {
        "success": f"Loaded model {current_index} successfully!",
        "architecture": str(weather_model)
    }

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
        ).cpu()
    output = denormalize_features(output).squeeze()

    return {
        "humidity" : output[0].item(),
        "pressure" : output[1].item(),
        "temperature" : output[2].item(),
        "wind_direction" : output[3].item(),
        "wind_speed" : output[4].item()
    }