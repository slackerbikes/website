Instructions:

++++++++++++++++++++++
Clone the repository

python3 -m venv new_env 

source new_env/bin/active

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py population_script.py

python manage.py runserver
