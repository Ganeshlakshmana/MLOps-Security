import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from Security.exception.exception import SecurityException
from Security.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

ca = certifi.where()


class DataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise SecurityException(e, sys) from e

    def csv_to_json_convertor(self, file_path):
        """
        Convert a CSV file to JSON format.
        """
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise SecurityException(e, sys) from e

    def push_data_to_mongodb(self, records, database_name, collection_name):
        try:
            # Use MongoDB Atlas TLS + Certifi
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=certifi.where()
            )

            self.db = self.mongo_client[database_name]
            collection = self.db[collection_name]

            result = collection.insert_many(records)
            return len(result.inserted_ids)

        except Exception as e:
            raise SecurityException(e, sys) from e


if __name__ == "__main__":
    file_path = r"DataSet\phisingData.csv"  
    database_name = "MLOpsDB"
    collection_name = "Phishing_Data"

    data_extractor = DataExtract()
    records = data_extractor.csv_to_json_convertor(file_path=file_path)
    num_records = data_extractor.push_data_to_mongodb(records, database_name, collection_name)
    
    print(f"Number of records inserted: {num_records}")
