from pymongo import MongoClient
from config.ressources import *

class DatabaseManager:
    """Provide methods and connection to the MongoDb database
    """

    __CONNECTION_STRING = str.format("mongodb+srv://{}:{}@{}/business?retryWrites=true&w=majority", MONGODB_USER, MONGODB_PASSWORD, MONGODB_SERVER )
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if DatabaseManager.__instance == None:
            DatabaseManager()
        return DatabaseManager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DatabaseManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DatabaseManager.__instance = self
            print(DatabaseManager.__CONNECTION_STRING)
            self.__client = MongoClient(DatabaseManager.__CONNECTION_STRING)

    def __get_collection(self, db_name, collection_name):
        """Generic method to connect to a given collection in a given database
        If the database or the collection don't exist, it will be created
        Args:
            db_name (str): name of the database
            collection_name (str): name of the collection
        Returns:
            collection: the collection
        """
        return self.__client.get_database(db_name).get_collection(collection_name)


    def get_country_by_name(self, name):
        """Get a country by its given name
        Args:
            name (str): name of the country
        Returns:
            json: informations about the country
        """
        return self.__get_collection('countries_project', 'countries').find_one({'Country': name})
