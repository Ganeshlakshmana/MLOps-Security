from datetime import datetime
import os
import sys

from Security.entity.config_entity import DataIngestionConfig
from Security.exception.exception import SecurityException
from Security.logging.logger import logging
from Security.constant import training_pipeline

print("Data Ingestion Component")


class TrainingPipelineConfig:
    def __init__(self, timestamp: datetime = datetime.now()):
        try:
            # Convert timestamp to readable folder format
            timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

            # Load constants from training_pipeline
            self.pipeline_name = training_pipeline.PIPELINE_NAME
            self.artifact_name = training_pipeline.ARTIFACT_DIR

            # Build final artifact directory:
            # pipeline_name/artifact/timestamp
            self.artifact_dir = os.path.join(
                self.pipeline_name,
                self.artifact_name,
                timestamp
            )

            # Store timestamp for reference
            self.timestamp: str = timestamp

        except Exception as e:
            raise SecurityException(e, sys) from e


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            # Root folder inside artifact directory
            self.data_ingestion_dir = os.path.join(
                training_pipeline_config.artifact_dir,
                training_pipeline.DATA_INGESTION_DIR_NAME
            )

            # MongoDB settings from constants
            self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
            self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME

            # Folder to store raw cleaned dataset
            self.feature_store_dir = os.path.join(
                self.data_ingestion_dir,
                training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
            )

            # Folder to store train-test split files
            self.ingested_dir = os.path.join(
                self.data_ingestion_dir,
                training_pipeline.DATA_INGESTION_INGESTED_DIR
            )

            # Train file path
            self.train_file_path = os.path.join(
                self.ingested_dir,
                training_pipeline.TRAIN_FILE_NAME
            )

            # Test file path
            self.test_file_path = os.path.join(
                self.ingested_dir,
                training_pipeline.TEST_FILE_NAME
            )

            # Train-test split ratio constant
            self.train_test_split_ratio = (
                training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
            )

        except Exception as e:
            raise SecurityException(e, sys) from e
