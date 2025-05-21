import pandas as pd
import torch

from torch.utils.data import Dataset


class WeatherDataset(Dataset):
    def __init__(self,
        lag_duration: int,
        city_coords: pd.DataFrame,
        *features: pd.DataFrame
    ):
        """
        :param int lag_duration: Duration of lag in days.
        :param pandas.DataFrame: The time-series features.
            These should have a consistent shape.
        """
        self._features = torch.stack([torch.tensor(df.to_numpy(), dtype=torch.float32) for df in features], dim=1)
        self._city_coords = torch.tensor(city_coords.to_numpy(), dtype=torch.float32)

        self._lag_duration = lag_duration
        self._total_sequences = self._features.shape[0] - self._lag_duration
        self._num_cities = self._features.shape[2]

    def __len__(self):
        return self._total_sequences * self._num_cities
    def __getitem__(self, idx: int):
        city_idx = idx // self._total_sequences
        time_idx = idx % self._total_sequences

        return (
            torch.concat([
                self._features[time_idx : time_idx + self._lag_duration, :, city_idx],
                self._city_coords[city_idx].repeat(self._lag_duration, 1)
            ], dim=1),
            self._features[time_idx + self._lag_duration, :, city_idx],
        )