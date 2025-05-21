import dataclasses

@dataclasses.dataclass
class Training_Config():
    random_state = 4
    batch_size = 32
    learning_rate = 1e-5
    epochs = 0
    lag_duration = 7

    def to_dict(self):
        return {
            'random_state': self.random_state,
            'batch_size': self.batch_size,
            'learning_rate': self.learning_rate,
            'epochs': self.epochs,
            'lag_duration': self.lag_duration,
        }