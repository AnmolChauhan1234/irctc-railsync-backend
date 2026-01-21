import os
from pymongo import MongoClient

class MongoService:
    _client = None
    _db = None

    @classmethod
    def get_db(cls):
        if cls._db is None:
            uri = os.getenv("MONGO_URI")
            db_name = os.getenv("MONGO_DB")

            cls._client = MongoClient(uri)
            cls._db = cls._client[db_name]

        return cls._db
        