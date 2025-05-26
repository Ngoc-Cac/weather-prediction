import torch

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.config import (
    APIConfig,
    MODEL_CONFIGS,
)
from api.data_models import (
    WeatherSequence,
    ModelOutput,
)
from api.utils import (
    denormalize_features,
    load_checkpoint,
    normalize_features,
)

from utils.lstm import LSTMRegressor



config = APIConfig(0,
    load_checkpoint(
        MODEL_CONFIGS[0]['checkpoint'],
        LSTMRegressor(**MODEL_CONFIGS[0]['params']),
        device='gpu' if torch.cuda.is_available() else 'cpu'
    ).eval()
)


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
        "model_index": config.model_index,
        "model": str(config.weather_model),
    }

@app.put("/set_model/{model_index}")
def set_model(model_index: int):
    """
    Set the current predicting model to a new one.
    """
    if model_index > len(MODEL_CONFIGS) - 1:
        raise HTTPException(status_code=404, detail=f"Model {model_index} not found! There are only {len(MODEL_CONFIGS)} models.")
    elif model_index < 0:
        raise HTTPException(status_code=400, detail="Cannot process negative model_index!")
    
    config.model_index = model_index
    config.weather_model = load_checkpoint(
        MODEL_CONFIGS[config.model_index]['checkpoint'],
        LSTMRegressor(**MODEL_CONFIGS[config.model_index]['params']),
        device=config.device
    ).eval()
    return {
        "success": f"Loaded model {config.model_index} successfully!",
        "architecture": str(config.weather_model)
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
        output = config.weather_model(
            torch.concat([normalize_features(in_features), city_coords], dim=1)
                 .to(config.device)
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