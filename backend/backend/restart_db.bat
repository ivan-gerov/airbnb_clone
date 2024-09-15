@echo off

REM Remove the database file
IF EXIST ..\db.sqlite3 (
    del ..\db.sqlite3
)

REM Remove the migrations folder if it exists
IF EXIST core\migrations (
    rmdir /s /q core\migrations
)

REM Create a new migrations folder
mkdir core\migrations

REM Create an empty __init__.py file
type nul > core\migrations\__init__.py

REM Run Django commands
python manage.py makemigrations
python manage.py migrate

