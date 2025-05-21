import torch

from fastapi import FastAPI

from data_models import (
    WeatherSequence,
    WeatherStats,
)


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/predict")
def predict(dates: WeatherSequence) -> WeatherStats:
    """
    Predict the weather statistics of the next day given a sequence
        of weather statistics at the specified location.
    """
    in_features = []
    for i, date in enumerate(dates):
        in_features.append([
            date.humidity, date.pressure, date.temperature,
            date.wind_direction, date.wind_speed
        ])
    in_features = torch.tensor(in_features)
    output = in_features.sum(0)

    return WeatherStats(
        humidity=output[0].item(),
        pressure=output[1].item(),
        temperature=output[2].item(),
        wind_direction=output[3].item(),
        wind_speed=output[4].item()
    )