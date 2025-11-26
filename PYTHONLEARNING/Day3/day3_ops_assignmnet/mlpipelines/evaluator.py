class Evaluator:
    def __init__(self, model, test_data):
        self.model = model
        self.test_data = test_data

    def evaluate(self):
        print("Evaluating model...")
        # Dummy evaluation: MAE
        errors = [abs(self.model - x) for x in self.test_data]
        return sum(errors) / len(errors)
