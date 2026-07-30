from pymongo import MongoClient
from typing import Dict, List, Union

class animalShelter(object):
    def __init__(self, username, password, host, database_name, collection_name, port, use_db=True):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database_name = database_name
        self.collection_name = collection_name
        self.use_db = use_db

        self.client = None
        self.database = None
        self.collection = None

    def _connect(self):
        if not self.use_db:
            print("skipping MongoDB connection.")
            return

        uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/"
        self.client = MongoClient(uri)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]
        print("Connected to MongoDB.")

    def create(self, data: Union[Dict, List[Dict]]) -> bool:
        if not self.use_db:
            print("DB disabled — create() skipped.")
            return False

        if isinstance(data, list):
            result = self.collection.insert_many(data)
            print(f"Successfully inserted {len(result.inserted_ids)} documents.")
            return True
        elif isinstance(data, dict):
            result = self.collection.insert_one(data)
            if result.inserted_id:
                print("Successfully inserted one document.")
                return True
            else:
                print("Failed to insert document.")
                return False
        else:
            raise TypeError("Data must be a dictionary or a list of dictionaries.")

    def read(self, query: Dict) -> List[Dict]:
        if not self.use_db:
            print("DB disabled — read() returning empty list.")
            return []

        results = list(self.collection.find(query))
        if results:
            print("Results:", results)
            return results
        else:
            print("No documents found matching the query.")
            return []

    def update(self, query: Dict, update_data: Dict) -> int:
        if not self.use_db:
            print("DB disabled — update() skipped.")
            return 0

        if not query:
            raise ValueError("Update query cannot be empty.")
        if not update_data:
            raise ValueError("Update data cannot be empty.")

        update_result = self.collection.update_many(query, {'$set': update_data})
        print(f"Successfully updated {update_result.modified_count} documents.")
        return update_result.modified_count

    def delete(self, query: Dict) -> int:
        if not self.use_db:
            print("DB disabled — delete() skipped.")
            return 0

        if not query:
            raise ValueError("Delete query cannot be empty.")

        delete_result = self.collection.delete_many(query)
        print(f"Successfully deleted {delete_result.deleted_count} documents.")
        return delete_result.deleted_count
