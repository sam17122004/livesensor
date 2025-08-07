from dataclasses import dataclass
import os
import pymongo
from dotenv import load_dotenv  # <-- Add this

load_dotenv()  # <-- Add this to load .env file

@dataclass
class EnvironmentVariables:
    MONGO_DB_URL: str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariables()

mongo_client = pymongo.MongoClient(env_var.MONGO_DB_URL)
database_name = "sensor"