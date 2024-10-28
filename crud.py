
from pymongo import MongoClient

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30050
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to insert a new document into the collection
    def create(self, data):
        """
        Inserts a document into the 'animals' collection
        :param data: dictionary containing document to insert
        :return: True if successful, False otherwise
        """
        if data is not None and isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred while inserting: {e}")
                return False
        else:
            raise Exception("Invalid data format. Data should be a non-empty dictionary.")

    # Read method to query for documents in the collection
    def read(self, query):
        """
        Queries for documents in the 'animals' collection
        :param query: dictionary containing key/value pairs for lookup
        :return: list of documents if successful, empty list otherwise
        """
        if query is not None and isinstance(query, dict):
            try:
                documents = list(self.collection.find(query))
                return documents if documents else []
            except Exception as e:
                print(f"An error occurred while querying: {e}")
                return []
        else:
            raise Exception("Invalid query format. Query should be a dictionary.")

    # Update method to modify documents in the collection
    def update(self, query, new_values):
        """
        Updates documents in the 'animals' collection based on the query and new values
        :param query: dictionary containing key/value pairs for lookup
        :param new_values: dictionary with the new data to update
        :return: number of documents updated
        """
        if query is not None and isinstance(query, dict) and new_values is not None and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(query, {'$set': new_values})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred while updating: {e}")
                return 0
        else:
            raise Exception("Invalid format. Both query and new_values should be dictionaries.")

    # Delete method to remove documents from the collection
    def delete(self, query):
        """
        Deletes documents from the 'animals' collection based on the query
        :param query: dictionary containing key/value pairs for lookup
        :return: number of documents deleted
        """
        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred while deleting: {e}")
                return 0
        else:
            raise Exception("Invalid query format. Query should be a dictionary.")
