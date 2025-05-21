from pydantic import (
    AfterValidator,
    BaseModel,
    Field,
)


from typing import (
    Annotated,
    Iterator,
)


def _validate_positive(number: int | float):
    if number < 0:
        raise ValueError("Got negative input...")
    return number
    
def _validate_humidity(humidity: float):
    if humidity < 0 or humidity > 100:
        raise ValueError("Humidity must be in range [0, 100]...")
    return humidity

def _validate_wind_dir(wind_direction: float):
    if wind_direction < 0 or wind_direction > 360:
        raise ValueError("Wind direction must be in range [0, 360]...")
    return wind_direction

def _validate_coords(geo_coords: tuple[float, float]):
    if abs(geo_coords[0]) > 90:
        raise ValueError("Latitude coordinates must be in range [-90, 90]")
    if abs(geo_coords[1]) > 180:
        raise ValueError("Latitude coordinates must be in range [-180, 180]")
    return geo_coords


class WeatherStats(BaseModel):
    """
    Weather statistics for the current date.
    """
    humidity: Annotated[float, AfterValidator(_validate_humidity)] =\
        Field(description="The humidity in percentage (0 - 100).")
    
    pressure: Annotated[float, AfterValidator(_validate_positive)] =\
        Field(description="The pressure in hPa.")
    
    temperature: Annotated[float, AfterValidator(_validate_positive)] =\
        Field(description="The temperature in Kelvins.")
    
    wind_direction: Annotated[float, AfterValidator(_validate_wind_dir)] =\
        Field(description="The wind direction in meteorological degrees (0 - 360).")
    
    wind_speed: Annotated[float, AfterValidator(_validate_positive)] =\
        Field(description="The wind speed in meters/second (m/s).")


class WeatherSequence(BaseModel):
    """
    Sequence of weather statistics for a maximum of seven days at a specified location.
    """
    city_coords: Annotated[tuple[float, float], AfterValidator(_validate_coords)] =\
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