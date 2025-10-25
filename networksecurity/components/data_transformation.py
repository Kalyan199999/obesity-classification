import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer    
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join( '../obesity_classification/models' , "preprocessor.pkl"  )

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):

        '''This function is responsible for data transformation'''
        
        try:
            
            num_cols = ['age', 'height', 'weight', 'fcvc', 'ncp', 'ch2o', 'faf', 'tue']
            
            cat_cols = ['gender','family_history_with_overweight','favc','caec','smoke','scc','calc','mtrans']

            num_pipeline = Pipeline( steps = [
                ( 'imputer', SimpleImputer( strategy = 'mean' ) ),
                ( 'scaler', StandardScaler() )
            ])

            cat_pipeline = Pipeline( steps = [
                ( 'imputer', SimpleImputer( strategy = 'most_frequent' ) ),
                ( 'one_hot_encoder', OneHotEncoder() )
            ])

            preprocessor = ColumnTransformer( 
                transformers=[
                    ("num_pipeline" , num_pipeline, num_cols ),
                    ("cat_pipeline", cat_pipeline, cat_cols )
                ]
             )
            
            return preprocessor
        
        except Exception as e:
            raise NetworkSecurityException(e)
        
        def initiate_data_transformation(self, train_path, test_path):

            try:
                df_train = pd.read_csv(train_path)

                df_test = pd.read_csv(test_path)

                logger.logging.info("Read train and test data completed")

                logger.logging.info("Obtaining preprocessing object")

                preprocessing_obj = self.get_data_transformer_object()

                target_column_name = 'target_label'

                input_feature_train_df = df_train.drop(columns=[target_column_name], axis=1)

                target_feature_train_df = df_train[target_column_name]

                input_feature_test_df = df_test.drop(columns=[target_column_name], axis=1)

            except Exception as e:
                raise NetworkSecurityException(e)