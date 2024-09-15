# Airbnb Clone 


## Prerequisites

- Python 3.8+

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Set up a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `env\scripts\activate`
5. Install the required packages: `pip install -r requirements.txt`

## Preparation

1. Navigate to the `backend` directory. `cd backend`
2. Run the script that sets up the database: `backend\restart_db.bat` 
3. Run the generate_sample_data command to populate the database with sample data: `python manage.py generate_sample_data`
4. OPTIONAL STEP - Create a superuser: `python manage.py createsuperuser --username admin --email` (it will ask for a password, enter 123 as it is easy)

## Running the Backend
* Start the Django server: `python manage.py runserver`

## Running the Frontend
1. Open a new terminal window on the root of the project.
2. Source the virtual environment: `env\scripts\activate`
3. Run `python -m http.server 3000`
4. Open your browser to `localhost:3000/frontend/`

