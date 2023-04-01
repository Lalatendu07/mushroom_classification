from mushroom_clf.utils import get_collection_as_dataframe
from mushroom_clf.entity import config_entity
from mushroom_clf.components.data_ingestion import DataIngestion 
from mushroom_clf.components.data_validation import DataValidation
from mushroom_clf.components.data_transformation import DataTransformation
from mushroom_clf.components.model_trainer import ModelTrainer
import os, sys

if __name__ == "__main__":
     try:
          #Data Ingestion
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
          
          #Data Validation
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation = DataValidation(data_validation_config=data_validation_config,
                            data_ingestion_artifact=data_ingestion_artifact)
          data_validation_artifact = data_validation.initiate_data_validation() 

          #Data Transformation
          data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
          data_transformation =  DataTransformation(data_transformation_config=data_transformation_config,
                                                    data_ingestion_artifact=data_ingestion_artifact)   
          data_transformation_artifact = data_transformation.initiate_data_transformation()

          #Model Trainer
          model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
          model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact = model_trainer.initiate_model_trainer()                                                       
     except Exception as e :
          print(e)

