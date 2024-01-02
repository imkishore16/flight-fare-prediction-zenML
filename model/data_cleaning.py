import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#parent class
class DataStrategy(ABC):
    """
    Abstract Class defining strategy for handling data
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass
    
# child class the extends DataStrategy
class DataPreprocessStrategy(DataStrategy):
    """
    Data preprocessing strategy which preprocesses the data.
    """
    
    def handle_data(self,data:pd.DataFrame)-> pd.DataFrame:
        """
        Removes columns which are not required, fills missing values with median average values/removes the missng value rows, and converts the data type to float.
        """
        try:
            # data=data.drop(["column1,column2"],axis=1)
            # data["column_name"].fillna(data["column_name"].median(), inplace=True)  
            data=data.dropna(inplace=True)
            return data
        except Exception as e:
            logging.error(e)
            raise e
        

# child class the extends DataStrategy 
class DataDivideStrategy(DataStrategy):
    """
    Data dividing strategy which divides the data into train and test data.
    """

    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        """
        Divides the data into train and test data.
        """
        try:
            X = data.drop("Price", axis=1)
            y = data["Price"]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            return X_train, X_test, y_train, y_test
        except Exception as e:
            logging.error(e)
            raise e
        

class DataCleaning:
    """
    Data cleaning class which preprocesses the data and divides it into train and test data.
    """
    # we have defined two different data stratergies above and wee need to pass which DataStratergy we are going to use
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy) -> None:
        """Initializes the DataCleaning class with a specific strategy."""
        self.df = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """Handle data based on the provided strategy"""
        return self.strategy.handle_data(self.df)


# we have defined two different data stratergies above and wee need to pass which DataStratergy we are going to use
# Example
if __name__ == "__main__":
    data=pd.read_eexcel()
    data_cleaning=DataCleaning(data,DataPreprocessStrategy())
    data_cleaning.handle_data()
    data_divide=DataCleaning(data,DataDivideStrategy())
    data_divide.handle_data()
    
