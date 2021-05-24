# Sunbasket Exercise

This application will retrieve a list of meals of a particular type for a given week. A date and meal type must be supplied, and if meals are available during the week of the given date, a JSON list of those meals will be returned.

## Setup
Note: This application was developed using Python 3.9. It is recommended to use a compatible version.

1. Make a new virtual environment `python -m venv venv`
2. Activate the virtual environment `source venv/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
4. In the project root run `cp .env.example .env`
5. Edit the `.env` file to add the database connection information

## Startup
Start the API server with `uvicorn main:app`. This should start a server running on `127.0.0.1:8000`.

## Use
Where `{date}` is a date in the format `YYYY-MM-DD` and `{meal_type}` is one of `MEAL_KIT`, `FRESH_READY`, or `PRE_PREPPED`, execute a GET request to `http://127.0.0.1:8000/menu/{date}/{meal_type}`. 

### Example
Request `http://127.0.0.1:8000/menu/2021-03-08/FRESH_READY`

Response
```
[
    "Spicy Southwestern turkey and sweet potato skillet",
    "Chicken cacciatore with spaghetti",
    "Chicken tikka masala with basmati rice pilaf"
]
```

## Testing
A test suite is available and can be run with `pytest test_main.py -v`

## Thoughts
If I were to expand this application, I would add additional endpoints to list all weeks with meals available (`/menu/`) all available meal types for a given week (`menu/{date}/meal_types`), and all available meals for a given week (`menu/{date}/meals`). This would give the user more information to provide a valid selection. 

The query for the `meal_type` list could be done at the start of the application and then memoized for later use. This would prevent repeated database queries for the same information which would not change regularly. That would introduce a need to be able to trigger a reload of `meal_type` data without restarting the entire application, most likely through another endpoint.