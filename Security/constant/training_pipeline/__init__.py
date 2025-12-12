import os
import sys
import numpy as np
import pandas as pd
from Security.exception.exception import SecurityException
from Security.logging.logger import logging

""" define constant variables for training pipeline"""

TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "security_detection_pipeline"
ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "phishingData.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

""" Data ingestion related constant start with DATA_INGESTION VARIABLES """



DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_COLLECTION_NAME :str = "phishing_data_collection"
DATA_INGESTION_DATABASE_NAME:str = "MLOpsDB"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float= 0.2
DATA_INGESTION_INGESTED_DIR:str  = "ingested_data"
        