Instructions:

Clone the Django application

venv -v env new_env

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py population_script.py

python manage.py runserver
