import os,sys
from datetime import datetime
from mushroom_clf.exception import MushroomException

FILE_NAME = 'mushroom.csv'
TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
MODEL_FILE_NAME = "model.pkl"
LABEL_ENCODER_OBJECT_FILE_NAME = "label_encoder.pkl"


class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}") 
        except Exception as e :
            raise MushroomException(e , sys)

class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "mushroom"
            self.collection_name = "mushroom_dataset"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.features_store_file_path = os.path.join(self.data_ingestion_dir,'features_store',FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,'dataset',TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,'dataset',TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e :
            raise MushroomException(e , sys)

    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise MushroomException(e, sys)        

class DataValidationConfig:
    
        def __init__(self,training_pipeline_config:TrainingPipelineConfig):
            try:
                self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
                self.report_file_path = os.path.join(self.data_validation_dir, "report.yaml")
                self.base_file_path = os.path.join("/config/workspace/agaricus-lepiota.data")
            except Exception as e :
                raise MushroomException(e, sys)


class DataTransformationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_transformation")
            self.transform_object_path = os.path.join(self.data_transformation_dir,"transformer",TRANSFORMER_OBJECT_FILE_NAME)
            self.transformed_train_path = os.path.join(self.data_transformation_dir,"transformed",TRAIN_FILE_NAME)
            self.transformed_test_path = os.path.join(self.data_transformation_dir,"transformed",TEST_FILE_NAME)
            self.label_encoder_path = os.path.join(self.data_transformation_dir,"label_encoder",LABEL_ENCODER_OBJECT_FILE_NAME)
        except Exception as e :
            raise MushroomException(e, sys)

class ModelTrainerConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir, "model_trainer")
            self.model_path = os.path.join(self.model_trainer_dir,"model", MODEL_FILE_NAME)
            self.expected_score = 0.7
            self.overfitting_thres = 0.1
        except Exception as e :
            raise MushroomException(e, sys)

class ModelEvaluationConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.change_threshold = 0.01
class ModelPusherConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.model_pusher_dir = os.path.join(training_pipeline_config.artifact_dir, "model_pusher")
            self.saved_model_dir = os.path.join("saved_models")
            self.pusher_model_dir = os.path.join(self.model_pusher_dir, "saved_models")
            self.pusher_model_path = os.path.join(self.pusher_model_dir,MODEL_FILE_NAME)
            self.pusher_transformer_path = os.path.join(self.pusher_model_dir,TRANSFORMER_OBJECT_FILE_NAME)
            self.pusher_label_encoder_path = os.path.join(self.pusher_model_dir,LABEL_ENCODER_OBJECT_FILE_NAME)
        except Exception as e:
            raise MushroomException(e, sys)    