import torch

from dataclasses import dataclass


MODEL_CONFIGS = [
    {
        'checkpoint': '../resource/models/lstm_only/4layer_cp3.tar',
        'params': {'in_features': 7, 'out_features': 5, 'num_layers': 4, 'fc_hidden_dims': ()},
    },
    {
        'checkpoint': '../resource/models/lstm_mlp/4layer_2mlp_cp4.tar',
        'params': {'in_features': 7, 'out_features': 5, 'num_layers': 4},
    },
]
@dataclass
class APIConfig():
    model_index: int
    weather_model: torch.nn.Module
    device: str = 'gpu' if torch.cuda.is_available() else 'cpu'