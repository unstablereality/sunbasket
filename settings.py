# Simple script to pull the database connection info from a .env file
# and load it for use in connecting to the database
# .env should be in the following format
# dbhost=hostname
# dbuser=username
# dbpass=password
# dbname=database_name

from dotenv import load_dotenv
import os

load_dotenv()

DBHOST = os.getenv("dbhost")
DBUSER = os.getenv("dbuser")
DBPASS = os.getenv("dbpass")
DBNAME = os.getenv("dbname")