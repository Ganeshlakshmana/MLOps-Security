from Security.components.data_ingestion import DataIngestion
from Security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from Security.exception.exception import SecurityException
from Security.logging.logger import logging

import sys

if __name__ == "__main__":
    try:
        logging.info("Starting the data ingestion process")

        # Initialize training pipeline configuration
        training_pipeline_config = TrainingPipelineConfig()

        # Initialize data ingestion configuration
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)

        # Create DataIngestion object
        data_ingestion = DataIngestion(data_ingestion_config)

        # Start data ingestion
        data_ingestion.initiate_data_ingestion()
        
        print("Data ingestion completed successfully.")

        logging.info("Data ingestion process completed successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise SecurityException(e, sys) from e