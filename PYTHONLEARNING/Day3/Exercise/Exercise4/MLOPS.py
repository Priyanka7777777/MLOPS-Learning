# -------------------------
# Base MLModel class
# -------------------------
class MLModel:
    def train(self, X, y):
        """Train the model."""
        pass

    def predict(self, X):
        """Make predictions."""
        pass

    def evaluate(self, X, y):
        """Evaluate the model."""
        pass


# -------------------------
# Simple Classifier using LogisticRegression
# -------------------------
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class SimpleClassifier(MLModel):
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X, y):
        preds = self.predict(X)
        return {"accuracy": accuracy_score(y, preds)}


# -------------------------
# Example usage
# -------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load simple dataset
data = load_iris()
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and use the model
model = SimpleClassifier()

model.train(X_train, y_train)
print("Training done!")

preds = model.predict(X_test)
print("Predictions:", preds)

metrics = model.evaluate(X_test, y_test)
print("Evaluation:", metrics)
