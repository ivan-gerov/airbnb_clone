rm ../db.sqlite3
rm -r core/migrations
mkdir core/migrations
touch core/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate

