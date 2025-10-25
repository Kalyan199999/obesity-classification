import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger
from networksecurity.utils.converting_target import    convert_target
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:

    path = '../obesity_classification/data'

    train_data_path: str = os.path.join( path , 'train.csv'  )
    test_data_path: str = os.path.join( path , 'test.csv'  )
    raw_data_path: str = os.path.join( path , 'ObesityDataSet.csv'  )

@dataclass
class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def intiate_data_ingestion(self):
        try:
            logger.logging.info(f"Loading the raw dataset from path: {self.ingestion_config.raw_data_path}")

            df = pd.read_csv(self.ingestion_config.raw_data_path)
            print(df.head())
            
            logger.logging.info(f"Dataset preview: \n{df.head()}")

            logger.logging.info(f"changing the columns into lower case!")
            df.columns = df.columns.str.lower()

            logger.logging.info(f"converting the target column into binary format!")
            df['target'] = df['nobeyesdad'].apply(convert_target)

            logger.logging.info(f"Deleting the column nobeyesdad!")
            df.drop('nobeyesdad', axis=1, inplace=True)

            logger.logging.info(f"Dataset preview after operations: \n{df.head()}")

            # make train and test paths
            os.makedirs( os.path.dirname( self.ingestion_config.train_data_path ), exist_ok=True )

            os.makedirs( os.path.dirname( self.ingestion_config.test_data_path ), exist_ok=True )

            train_df,test_df = train_test_split(df, test_size=0.2, random_state=42)

            logger.logging.info(f"Train and test data is split into train and test data initiated!")

            train_df.to_csv(self.ingestion_config.train_data_path, index=False)

            test_df.to_csv(self.ingestion_config.test_data_path, index=False)

            logger.logging.info(f"Train and test data is split is done!")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            raise NetworkSecurityException(e)
        

# if __name__ == "__main__":
#     obj = DataIngestion()
#     obj.intiate_data_ingestion()