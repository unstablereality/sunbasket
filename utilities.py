from fastapi import HTTPException
from datetime import datetime
import mysql.connector
import settings


# Initiate the database connection and return the db_conn object
def db_connect():
    # Import the database connection info from settings
    dbinfo = {
        "db_host": settings.DBHOST,
        "db_user": settings.DBUSER,
        "db_pass": settings.DBPASS,
        "db_name": settings.DBNAME,
    }

    # Create the database connection
    db_conn = mysql.connector.connect(
        host=dbinfo["db_host"],
        user=dbinfo["db_user"],
        password=dbinfo["db_pass"],
        database=dbinfo["db_name"],
    )
    return db_conn


# Validate the date format is correct, otherwise raise a 400
def validate_date(date):
    date_format = "%Y-%m-%d"

    try:
        datetime.strptime(date, date_format)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")


# Validate the meal type is valid, otherwise raise a 400
def validate_meal_type(meal_type, db_conn):
    # Get the list of meal types from the database
    meal_type_list = []
    query = "SELECT DISTINCT(type) FROM meal"
    cursor = db_conn.cursor()
    cursor.execute(query)
    for item in cursor:
        meal_type_list.append(item[0])

    # Check that meal_type_list is in meal_type_list
    if meal_type not in meal_type_list:
        raise HTTPException(status_code=400, detail="Invalid meal type")
