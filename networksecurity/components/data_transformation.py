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
from networksecurity.utils.converting import convert_cat_col_lower , save_object
from networksecurity.components.data_ingestion import DataIngestion

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join( '../obesity_classification/models' , "preprocessor.pkl"  )


@dataclass
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self,num_cols,cat_cols):

        '''This function is responsible for data transformation'''
        
        try:
            
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
            
            num_cols = ['age', 'height', 'weight', 'fcvc', 'ncp', 'ch2o', 'faf', 'tue']
            
            cat_cols = ['gender','family_history_with_overweight','favc','caec','smoke','scc','calc','mtrans']
            
            logger.logging.info("Reading the training and testing data!")
            
            df_train = pd.read_csv(train_path)
            
            df_test = pd.read_csv(test_path)
            
            logger.logging.info("Reading train and test data completed")
            
            logger.logging.info("Converting categorical columns to lowercase!")
            
            df_train = convert_cat_col_lower( X=df_train , cat_cols=cat_cols )
            
            df_test = convert_cat_col_lower( X=df_test , cat_cols=cat_cols )
            
            logger.logging.info("Obtaining preprocessing object")
            
            preprocessing_obj = self.get_data_transformer_object(num_cols=num_cols, cat_cols=cat_cols)
            
            target_column_name = 'target'
            
            logger.logging.info("Seperating the independent and dependent features for training and testing!")
            
            input_feature_train_df = df_train.drop(columns=[target_column_name], axis=1)
            
            target_feature_train_df = df_train[target_column_name]
            
            input_feature_test_df = df_test.drop(columns=[target_column_name], axis=1)
            
            target_feature_test_df = df_test[target_column_name]
            
            logger.logging.info("Applying preprocessing object on training dataframe and testing dataframe")
            
            input_feature_train_transformed = preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_transformed = preprocessing_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_transformed, np.array(target_feature_train_df)
            ]
            
            test_arr = np.c_[
                input_feature_test_transformed, np.array(target_feature_test_df)
            ]


            save_object( file_path =self.data_transformation_config.preprocessor_obj_file_path , obj = preprocessing_obj )

            logger.logging.info("Preprocessing object saved")
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
            raise NetworkSecurityException(e)
        

# if __name__ == '__main__':

#     di = DataIngestion()

#     train_path , test_path , _ = di.intiate_data_ingestion()

#     dt = DataTransformation()
    
#     dt.initiate_data_transformation(train_path=train_path, test_path=test_path)