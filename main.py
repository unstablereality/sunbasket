from datetime import datetime
from fastapi import FastAPI, HTTPException
import mysql.connector
import settings

# Fire up a new API
app = FastAPI()


# Get the list of meal names for a given date and type
@app.get("/menu/{date}/{meal_type}")
async def get_meal_names(date, meal_type):
    payload = []

    # Set up the query using the path parameters
    query = (f"SELECT meal.name FROM meal "
             f"JOIN meal_week mw ON meal.id = mw.meal_id "
             f"JOIN week w on mw.week_id = w.id "
             f"WHERE type = '{meal_type}' "
             f"AND '{date}' BETWEEN w.start_date AND w.end_date")

    # Connect to the DB
    db_conn = db_connect()

    # Validate the input
    validate_date(date)
    validate_meal_type(meal_type, db_conn)

    # Execute the query
    cursor = db_conn.cursor()
    cursor.execute(query)

    # Iterate the results and build the payload
    for item in cursor:
        payload.append(item[0])

    # Validate the payload
    validate_payload(payload)

    # Clean up the database connection
    db_conn.close()

    # Escort the payload
    return payload


# Initiate the database connection and return the db_conn object
def db_connect():
    # Import the database connection info from settings
    dbinfo = {'db_host': settings.DBHOST,
              'db_user': settings.DBUSER,
              'db_pass': settings.DBPASS,
              'db_name': settings.DBNAME}

    # Create the database connection
    db_conn = mysql.connector.connect(host=dbinfo['db_host'],
                                      user=dbinfo['db_user'],
                                      password=dbinfo['db_pass'],
                                      database=dbinfo['db_name'])
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


# Validate that we got some results, otherwise raise a 404
def validate_payload(payload):
    if not payload:
        raise HTTPException(status_code=404, detail="No meals found")
