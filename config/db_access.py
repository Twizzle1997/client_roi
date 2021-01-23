from pymongo import MongoClient
from config.ressources import *
import random
import datetime
import ast

class DatabaseManager:
    """Provide methods and connection to the MongoDb database
    """

    __CONNECTION_STRING = str.format("mongodb+srv://{}:{}@{}", MONGODB_USER, MONGODB_PASSWORD, MONGODB_SERVER)
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
            raise Exception("This class is a singleton.")
        else:
            DatabaseManager.__instance = self
            print(DatabaseManager.__CONNECTION_STRING)
            self.__client = MongoClient(DatabaseManager.__CONNECTION_STRING)


    def __get_collection(self, db_name, collection_name):
        """Generic method to connect to a given collection in a given database
        If the database or the collection doesn't exist, it will be created.
        Args:
            db_name (str): name of the database.
            collection_name (str): name of the collection.
        Returns:
            collection: the collection.
        """
        return self.__client.get_database(db_name).get_collection(collection_name)


    def get_country_by_name(self, name):
        """Get a country by its given name.
        Args:
            name (str): name of the country.
        Returns:
            json: informations about the country.
        """

        return self.__get_collection('countries_project', 'countries').find_one({'country': name})

    def set_country(self, name):
        """Add a new country to the databse with random informations.
        Args:
            name (str): name of the country.
        Returns:
            json: informations about the new country created.
        """

        density = random.randint(10, 1000)
        land_area = random.randint(100000, 1000000)
        pop = random.randint(10000, 10000000)

        country={"country": name, 
                    "density": density, 
                    "area": land_area, 
                    "pop": pop, 
                    "last_update" : datetime.datetime.now(),
                    }

        self.__get_collection('countries_project', 'countries').insert_one(country)

        return self.get_country_by_name(name)

    def delete_country_by_name(self, name):
        """Delete a country by its name.
        Args:
            name (str): name of the country.
        Returns:
            json: confirmation message.
        """

        self.__get_collection('countries_project', 'countries').remove({'country': name})

        return {"Message": "The country has been deleted."}


    def update_country_by_name(self, name, data):
        """Update a country by its name.
        Args:
            name (str): name of the country.
            data (dictionnary): list of key/value to update.
        Returns:
            json: updated country.
        """

        asked = {"country": name}
        values = {"$set": data}
        date = {"$set": {"last_update" : datetime.datetime.now()}}
                
        self.__get_collection('countries_project', 'countries').update_one(asked, [values, date])

        return self.get_country_by_name(name)

    def get_countries_class(self):
        """Classifies the countries regarding their density rank. 

        Returns:
            json: all the database's countries classified into four density range.
        """

        filter1 = {'density': {"$lt" : 50}}
        filter2 = {'density': {"$gt" : 50, "$lt" : 133}}
        filter3 = {'density': {"$gt" : 133, "$lt" : 350}}
        filter4 = {'density': {"$gt" : 350}}

        dict1 = self.__get_collection('countries_project', 'countries').find(filter1)
        dict2 = self.__get_collection('countries_project', 'countries').find(filter2)
        dict3 = self.__get_collection('countries_project', 'countries').find(filter3)
        dict4 = self.__get_collection('countries_project', 'countries').find(filter4)


        return {'Très peu denses' : dict1, 'Peu denses' : dict2, 'Densité intermédiaire' : dict3, 'Densément peuplés' : dict4}

