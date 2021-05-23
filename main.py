from fastapi import FastAPI
from utilities import (
    db_connect,
    validate_date,
    validate_payload,
    validate_meal_type
)


# Fire up a new API
app = FastAPI()


# Get the list of meal names for a given date and type
@app.get("/menu/{date}/{meal_type}")
def get_meal_names(date, meal_type):
    payload = []

    # Set up the query using the path parameters
    query = (
        f"SELECT meal.name FROM meal "
        f"JOIN meal_week mw ON meal.id = mw.meal_id "
        f"JOIN week w on mw.week_id = w.id "
        f"WHERE type = '{meal_type}' "
        f"AND '{date}' BETWEEN w.start_date AND w.end_date"
    )

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
