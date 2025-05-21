import torch

from utils.lstm import LSTMRegressor


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