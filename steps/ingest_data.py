import logging

import pandas as pd
from zenml import step

class IngestData:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self) -> None:
        """Initialize the data ingestion class."""
        pass

    def get_data(self) -> pd.DataFrame:
        df = pd.read_excel("D:\Visual Studio 2019\Data Science\Predict Fare of Airlines\zenml flight fare prediction\data\dataset.xlsx")
        
        return df

@step
def ingest_data() -> pd.DataFrame:
    """
    Args:
        None
    Returns:
        df: pd.DataFrame
    """
    try:
        ingest_data = IngestData()
        df = ingest_data.get_data()
        print(df.head())
        return df
    except Exception as e:
        logging.error(e)
        raise e