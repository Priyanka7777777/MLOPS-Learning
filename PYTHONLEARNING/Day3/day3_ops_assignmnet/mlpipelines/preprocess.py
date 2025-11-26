class Preprocessor:
    def __init__(self, data):
        self.data = data

    def clean(self):
        print("Cleaning data...")
        # Example: remove None values
        cleaned = [x for x in self.data if x is not None]
        return cleaned

    def normalize(self, data):
        print("Normalizing data...")
        mn = min(data)
        mx = max(data)
        return [(x - mn) / (mx - mn) for x in data]
