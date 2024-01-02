from steps.clean_data import clean_data
from steps.evaluate_model import evaluate_model
from steps.ingest_data import ingest_data
from steps.model_train import train_model

from pipelines.training_pipeline import train_pipeline

if __name__=="__main__":
    # path="./data/dataset.xlsx"
    training = train_pipeline(
        ingest_data(),
        clean_data(),
        train_model(),
        evaluate_model(),
    )
    print("00000000000000")
    training.run()
    
    # print(
    #     "Now run \n "
    #     f"    mlflow ui --backend-store-uri '{get_tracking_uri()}'\n"
    #     "To inspect your experiment runs within the mlflow UI.\n"
    #     "You can find your runs tracked within the `mlflow_example_pipeline`"
    #     "experiment. Here you'll also be able to compare the two runs.)"
    # )