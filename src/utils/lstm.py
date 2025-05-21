import torch

from torch import nn


class LSTMRegressor(nn.Module):
    def __init__(self,
        in_features: int,
        out_features: int,
        hidden_size: int = 512,
        num_layers: int = 2,
        fc_hidden_dims: tuple[int] = (512, 512),
        activation_fn: nn.Module | None = None
    ):
        super().__init__()
        if activation_fn is None:
            activation_fn = nn.ReLU()

        self._lstm_block = nn.LSTM(
            input_size=in_features,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        self._fc = nn.Sequential()
        for i, dim in enumerate(fc_hidden_dims):
            self._fc.add_module(str(i),
                nn.Sequential(
                    nn.Linear(
                        hidden_size if i == 0 else fc_hidden_dims[i - 1],
                        dim
                    ),
                    nn.BatchNorm1d(dim),
                    activation_fn
                )
            )
        self._fc.add_module("out", nn.Linear(fc_hidden_dims[-1] if fc_hidden_dims else hidden_size, out_features))

    def forward(self, sequence, hidden_cell_states=None):
        return self._fc(
            self._lstm_block(
                sequence, hidden_cell_states
            )[0][:, -1, :]
        )