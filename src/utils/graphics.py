import torch
import matplotlib.pyplot as plt

from numpy.typing import ArrayLike
from matplotlib.axes import Axes

def draw_series(
    ground_truth: ArrayLike,
    predictions: torch.Tensor,
    lag_dur: int = 0,
    ax: Axes | None = None,
    xlabel: str ='',
    ylabel: str = '',
):
    if lag_dur == 0 and len(ground_truth) != len(predictions):
        raise ValueError("Mismatch length between ground_truth and predictions with zero lag...")
    if ax is None:
        ax = plt.gca()
        
    no_day = len(ground_truth)
    ax.plot(ground_truth, color='blue', label='Ground truth')
    ax.plot(
        list(range(lag_dur, no_day)) if lag_dur != 0 else list(range(len(predictions))),
        predictions, color='orange', label='Prediction'
    )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax