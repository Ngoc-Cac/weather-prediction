import torch

from fastapi import FastAPI

from api.load_model import load_checkpoint
from api.data_models import (
    WeatherSequence,
    WeatherStats,
)

from utils.lstm import LSTMRegressor


weather_model = load_checkpoint(
    '../resource/models/lstm_only/4layer_cp3.tar',
    LSTMRegressor(7, 5, num_layers=4, fc_hidden_dims=()),
    device='gpu' if torch.cuda.is_available() else 'cpu'
)


app = FastAPI()


@app.put("/predict/")
def predict(date_sequence: WeatherSequence) -> WeatherStats:
    """
    Predict the weather statistics of the next day given a sequence
        of weather statistics at the specified location.
    """
    in_features = [[
            stats.humidity, stats.pressure, stats.temperature,
            stats.wind_direction, stats.wind_speed,
            *date_sequence.city_coords
        ] for stats in date_sequence
    ]
    output = weather_model(torch.tensor(in_features).unsqueeze(0)).squeeze()

    return WeatherStats(
        humidity=output[0].item(),
        pressure=output[1].item(),
        temperature=output[2].item(),
        wind_direction=output[3].item(),
        wind_speed=output[4].item()
    )