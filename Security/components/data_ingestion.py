from Security.exception.exception import SecurityException
from Security.logging.logger import logging
from Security.entity.config_entity import DataIngestionConfig

import os
import sys
import pandas as pd
import numpy as np
import pymongo
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SecurityException(e, sys) from e

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        try:
            logging.info("Exporting MongoDB collection as DataFrame")

            mongo_client = pymongo.MongoClient(
    MONGO_DB_URL,
    serverSelectionTimeoutMS=30000
)

            database = mongo_client[self.data_ingestion_config.database_name]
            collection = database[self.data_ingestion_config.collection_name]

            data = list(collection.find())
            logging.info(f"Fetched {len(data)} records")

            df = pd.DataFrame(data)

            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            df.replace(to_replace=np.nan, value=pd.NA, inplace=True)

            mongo_client.close()
            return df

        except Exception as e:
            raise SecurityException(e, sys) from e

    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion")

            df = self.export_collection_as_dataframe()

            # Feature store
            os.makedirs(self.data_ingestion_config.feature_store_dir, exist_ok=True)
            feature_store_path = os.path.join(
                self.data_ingestion_config.feature_store_dir,
                "feature_store.csv"
            )
            df.to_csv(feature_store_path, index=False)

            logging.info(f"Feature store saved at {feature_store_path}")

            # Train-test split
            train_set, test_set = train_test_split(
                df,
                test_size=self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )

            os.makedirs(self.data_ingestion_config.ingested_dir, exist_ok=True)

            train_path = os.path.join(
                self.data_ingestion_config.ingested_dir, "train.csv"
            )
            test_path = os.path.join(
                self.data_ingestion_config.ingested_dir, "test.csv"
            )

            train_set.to_csv(train_path, index=False)
            test_set.to_csv(test_path, index=False)

            logging.info("Data ingestion completed successfully")

            return {
                "feature_store": feature_store_path,
                "train_file": train_path,
                "test_file": test_path
            }

        except Exception as e:
            raise SecurityException(e, sys) from e
