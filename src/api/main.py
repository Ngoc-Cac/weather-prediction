import torch

from fastapi import FastAPI

from data_models import (
    WeatherSequence,
    WeatherStats,
)


app = FastAPI()


@app.put("/predict")
def predict(date_sequence: WeatherSequence) -> WeatherStats:
    """
    Predict the weather statistics of the next day given a sequence
        of weather statistics at the specified location.
    """
    in_features = [[
            stats.humidity, stats.pressure, stats.temperature,
            stats.wind_direction, stats.wind_speed
        ] for stats in date_sequence
    ]
    in_features = torch.tensor(in_features)
    output = in_features.sum(0)

    return WeatherStats(
        humidity=output[0].item(),
        pressure=output[1].item(),
        temperature=output[2].item(),
        wind_direction=output[3].item(),
        wind_speed=output[4].item()
    )