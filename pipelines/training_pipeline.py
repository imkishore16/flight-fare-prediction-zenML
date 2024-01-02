from zenml.config import DockerSettings
from zenml.integrations.constants import MLFLOW
from zenml.pipelines import pipeline

@pipeline(enable_cache=True)
def train_pipeline(ingest_data, clean_data, model_train, evaluate_model):
    """
    Args:
        ingest_data: DataClass
        clean_data: DataClass
        model_train: DataClass
        evaluation: DataClass
    Returns:
        mse: float
        rmse: float
    """
    print("11111111111111")
    df = ingest_data()
    print("22222222222222")
    print(df.head())
    x_train, x_test, y_train, y_test = clean_data(df)
    model = model_train(x_train, x_test, y_train, y_test)
    mse, rmse = evaluate_model(model, x_test, y_test)