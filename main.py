from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

DBHOST = os.getenv("dbhost")
DBUSER = os.getenv("dbuser")
DBPASS = os.getenv("dbpass")
DBNAME = os.getenv("dbname")

app = FastAPI()

# Get the list of meal names for a given date and type

# The API should accept a GET request at /menu/<YYYY-MM-DD>/<type>
# For example: GET /menu/2021-03-03/MEAL_KIT
# The response should be a JSON list of meal names of the type,
# that are available on that date. For
# example:["Tomato-braised chicken with sweet potato and chard", "Miso-ginger
# ground pork and summer squash donburi", ... ]
# If there are no meals available, the response should be an HTTP 404 error.