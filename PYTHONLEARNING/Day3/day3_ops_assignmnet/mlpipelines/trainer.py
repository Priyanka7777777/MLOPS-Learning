class Trainer:
    def __init__(self, data):
        self.data = data
        self.model = None

    def train(self):
        print("Training model...")
        # Dummy model: mean value
        self.model = sum(self.data) / len(self.data)
        return self.model
