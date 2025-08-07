from sensor.exception import SensorException
import sys
import os

from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongodb_collection


# def test_sensor_exception():
#     try:
#         logging.info(" Testing SensorException")
#         a=1/0  # This will raise a ZeroDivisionError
#     except Exception as e:
#            raise SensorException(e, sys) 

# if __name__ == "__main__":
#     try:
#         test_sensor_exception()
#     except Exception as e:
#         print(e)  # This will print the formatted error message
# if __name__ == "__main__":
#     file_path="C:/Users/palla/Desktop/sensorlive/aps_failure_training_set1.csv"
#     database_name="Sambeet"
#     collection_name="sensor"
#     dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)  
# filepath: c:\Users\palla\Desktop\sensorlive\main.py
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    pipeline_config = TrainingPipelineConfig()
    ingestion_config = DataIngestionConfig(pipeline_config)
    data_ingestion = DataIngestion(ingestion_config)
    artifact = data_ingestion.initiate_data_ingestion()
    print("Artifacts created at:", pipeline_config.artifact_dir)

from sensor.components.data_validation import DataValidation
from sensor.entity.config_entity import TrainingPipelineConfig, DataValidationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
if __name__ == "__main__":
    pipeline_config = TrainingPipelineConfig()
    
    ingestion_config = DataIngestionConfig(pipeline_config)
    data_ingestion = DataIngestion(ingestion_config)
    ingestion_artifact = data_ingestion.initiate_data_ingestion()

    validation_config = DataValidationConfig(pipeline_config)
    data_validation = DataValidation(ingestion_artifact, validation_config)
    validation_artifact = data_validation.initiate_data_validation()
    
    print("Data validation completed. Artifacts created at:", pipeline_config.artifact_dir)
