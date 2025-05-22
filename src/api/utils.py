import torch
import pandas as pd

from utils.lstm import LSTMRegressor


_temp = pd.read_csv('../resource/dataset/train-test-split/metascale.csv', index_col=0)
_minimums = torch.tensor(_temp.loc['min'].to_numpy(), dtype=torch.float32)
_difference = torch.tensor(_temp.loc['max'].to_numpy(), dtype=torch.float32) - _minimums


def load_checkpoint(
    checkpoint: str,
    model: LSTMRegressor,
    device: str,
):
    model.load_state_dict(
        torch.load(
            checkpoint,
            map_location=device,
            weights_only=False
        )['model']
    )
    return model

def normalize_features(features: torch.Tensor) -> torch.Tensor:
    repeated_min = _minimums.repeat(features.shape[0], 1)
    repeated_diff = _difference.repeat(features.shape[0], 1)
    return (features - repeated_min) / repeated_diff