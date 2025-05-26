import torch

from pydantic import (
    AfterValidator,
    BaseModel,
    Field,
)


from typing import (
    Annotated,
    Iterator,
    TypeAlias
)

Numeric: TypeAlias = int | float


def _validate_non_neg(number: Numeric):
    if number < 0:
        raise ValueError("Got negative input...")
    return number
    
def _validate_humidity(humidity: Numeric):
    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity must be in range [0, 100]...")
    return humidity

def _validate_wind_dir(wind_direction: Numeric):
    if wind_direction < 0 or wind_direction > 360:
        raise ValueError("Wind direction must be in range [0, 360]...")
    return wind_direction

def _validate_coords(geo_coords: tuple[Numeric, Numeric]):
    if len(geo_coords) != 2:
        raise ValueError("Coordinates must contain exactly two numbers, given as (latitude, longitude)...")
    if abs(geo_coords[0]) > 90:
        raise ValueError("Latitude coordinates must be in range [-90, 90]...")
    if abs(geo_coords[1]) > 180:
        raise ValueError("Latitude coordinates must be in range [-180, 180]...")
    return geo_coords


class ModelOutput(BaseModel):
    """
    Unbounded predicted values for the next day. These values carry the same
        semantic with WeatherStats with the exception that they may or may not
        lie within the allowed value range.
    """
    humidity: Numeric
    pressure: Numeric
    temperature: Numeric
    wind_direction: Numeric
    wind_speed: Numeric

class WeatherStats(BaseModel):
    """
    Weather statistics for the current date.
    """
    humidity: Annotated[Numeric, AfterValidator(_validate_humidity)] =\
        Field(description="The humidity in percentage (0 - 100).")
    
    pressure: Annotated[Numeric, AfterValidator(_validate_non_neg)] =\
        Field(description="The pressure in hPa.")
    
    temperature: Annotated[Numeric, AfterValidator(_validate_non_neg)] =\
        Field(description="The temperature in Kelvins.")
    
    wind_direction: Annotated[Numeric, AfterValidator(_validate_wind_dir)] =\
        Field(description="The wind direction in meteorological degrees (0 - 360).")
    
    wind_speed: Annotated[Numeric, AfterValidator(_validate_non_neg)] =\
        Field(description="The wind speed in meters/second (m/s).")


class WeatherSequence(BaseModel):
    """
    Sequence of weather statistics for a maximum of seven days at a specified location.
    """
    city_coords: Annotated[tuple[Numeric, Numeric], AfterValidator(_validate_coords)] =\
        Field(description="Coordinates of the location given as (latitude, longitude)")
    
    day_1: WeatherStats = Field(description="The weather statistics of the first day in the sequence.")
    day_2: WeatherStats | None = Field(None, description="Optional weather statistics of the second day in the sequence.")
    day_3: WeatherStats | None = Field(None, description="Optional weather statistics of the third day in the sequence.")
    day_4: WeatherStats | None = Field(None, description="Optional weather statistics of the fourth day in the sequence.")
    day_5: WeatherStats | None = Field(None, description="Optional weather statistics of the fifth day in the sequence.")
    day_6: WeatherStats | None = Field(None, description="Optional weather statistics of the sixth day in the sequence.")
    day_7: WeatherStats | None = Field(None, description="Optional weather statistics of the seventh day in the sequence.")

    def __iter__(self) -> Iterator[WeatherStats]:
        dates = [
            self.day_1, self.day_2, self.day_3,
            self.day_4, self.day_5, self.day_6,
            self.day_7
        ]
        for stats in dates:
            if not stats is None:
                yield stats

    def to_tensor(self):
        in_features = torch.tensor([[
                stats.humidity, stats.pressure, stats.temperature,
                stats.wind_direction, stats.wind_speed,
            ] for stats in self
        ], dtype=torch.float32)
        return torch.concat(
            [
                in_features,
                torch.tensor(self.city_coords, dtype=torch.float32)\
                     .repeat(in_features.shape[0], 1)
            ],
            dim=1
        )