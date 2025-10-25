from networksecurity.logging import logger
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.utils.converting import save_object

import os,sys

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.svm import SVC

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_obj_file_path = os.path.join( '../obesity_classification/models' , "svc.pkl"  )

class ModelTrainer:
    def __init__(self):
        self.model_trainer_path = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            
            logger.logging.info("Data splitting Started!")
            
            X_train,y_train = train_array[:,:-1],train_array[:,-1]

            X_test,y_test = test_array[:,:-1],test_array[:,-1]

            logger.logging.info("Data Splitting Done!")

            logger.logging.info("Model Training Started!")

            model = SVC()
            model.fit(X_train,y_train)

            logger.logging.info("Model Training Done!")
            
            logger.logging.info("Model Evaluation Started!")

            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test,y_pred)
            classificationReport = classification_report(y_test,y_pred)
            confusionMatrix = confusion_matrix(y_test,y_pred)

            logger.logging.info(f"Accuracy of the model is : {accuracy}")

            logger.logging.info(f"classification Report of the model is :\n {classificationReport}")
            
            logger.logging.info(f"confusion matrix of the model is : {confusionMatrix}")
            
            logger.logging.info("Model Evaluation Done!")

            logger.logging.info("Model Saving Started!")

            save_object( file_path=self.model_trainer_path.model_obj_file_path , obj=model)

            logger.logging.info("Model Saving Done!")

            return(
                self.model_trainer_path.model_obj_file_path
            )


        except Exception as e:
            raise NetworkSecurityException(e)
        

if __name__ == "__main__":

    di = DataIngestion()

    train_path , test_path , _ = di.intiate_data_ingestion()

    dt = DataTransformation()
    
    train_arr,test_arr,preprocessor_obj_file_path = dt.initiate_data_transformation(train_path=train_path, test_path=test_path)

    mt = ModelTrainer()

    mt.initiate_model_trainer(train_arr, test_arr)