from pymongo import MongoClient
# --------------------------
# Backend: MongoDB Animal Shelter Class (mock database)
# --------------------------
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

    def _connect(self) -> None:
        """

        :rtype: None
        """
        if not self.use_db:
            print("skipping MongoDB connection.")
            return

        uri = f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/"
        self.client = MongoClient(uri)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]
        

    