from mlpipelines.preprocess import Preprocessor
from mlpipelines.trainer import Trainer
from mlpipelines.evaluator import Evaluator

if __name__ == "__main__":
    raw_data = [10, 20, None, 30, 40, None, 50]

    print("=== ML Pipeline Started ===")

    # Preprocessing
    pre = Preprocessor(raw_data)
    cleaned = pre.clean()
    normalized = pre.normalize(cleaned)

    # Training
    trainer = Trainer(normalized)
    model = trainer.train()

    # Evaluation
    test_data = [0.2, 0.5, 0.8]
    evaluator = Evaluator(model, test_data)
    score = evaluator.evaluate()

    print("\nModel Value:", model)
    print("Evaluation Score (MAE):", score)
    print("=== Pipeline Completed ===")
