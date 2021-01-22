from dotenv import load_dotenv
import os

load_dotenv('.env')

MONGODB_USER = os.getenv("MONGO_USER")
MONGODB_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGODB_SERVER = "cluster0.5dfy0.mongodb.net"
