# Le client est roi  

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
  * [Routes](#routes)
  * [Settings](#settings)

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com)
* [PyMongo](https://pymongo.readthedocs.io)

<!-- GETTING STARTED -->
## Getting Started

Get a local copy up and running following these steps.

### Installation

1. Clone the repository :

    ```sh
    git clone https://github.com/Twizzle1997/client_roi
    ```
    
2. Create a .env file with the two variables : ```MONGO_USER``` and ```MONGO_PASSWORD```  
3. Install the requirements :
    ```sh
    pip install -r requirements.txt
    ```
    ```sh
    conda create --name <env_name> --file requirements.txt
    ```


<!-- USAGE EXAMPLES -->
## Usage

* Run [main.py](https://github.com/Twizzle1997/client_roi/blob/main/main.py) to start the app.  
* Oppen [tests.ipynb](https://github.com/Twizzle1997/client_roi/blob/main/tests.ipynb) to read the API tests and make some new ones.  
* The API will be launched on port 8080.

### Routes
* ```/api/request/<name>``` *(**GET** method)* get information about a country.  
* ```/api/add``` *(**POST** method, name:str)* add a fictive country to the database.    
* ```/api/remove``` *(**DELETE** method, name:str)* delete a country of the dataset.  
* ```/api/update``` *(**PUT** method, name:str, couple:str)* update informations about a country.  
* ```/api/class``` *(**GET** method)* classifies all the database countries regarding their density ranks. 

### Settings
* [config > ressources.py](https://github.com/Twizzle1997/client_roi/blob/main/config/ressources.py) contains the connection settings.   
* [config > db_access.py](https://github.com/Twizzle1997/client_roi/blob/main/config/db_access.py) provides the methods and connection to the MongoDb database.

