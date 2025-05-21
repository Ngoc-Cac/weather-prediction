import dataclasses

@dataclasses.dataclass
class Training_Config():
    random_state = 4
    batch_size = 32
    learning_rate = 1e-5
    epochs = 0
    lag_duration = 7