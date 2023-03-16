from mushroom_clf.utils import get_collection_as_dataframe
from mushroom_clf.entity import config_entity
from mushroom_clf.components.data_ingestion import DataIngestion 
import os, sys

if __name__ == "__main__":
     try:
          #Data Ingestion
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
     except Exception as e :
          print(e)

