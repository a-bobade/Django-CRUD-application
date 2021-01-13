# Django-CRUD-application
A simple Django CRUD application. 

# Project Summary
The application displays students record, where you can create a new record, update an existing record, view a record or delete a record.\
You can also search for a student record using the student's matric number.

# Running this project
- To get this project up and running you should start by having Python installed on your computer. 

- Activate the virtual environment with:\
  venv\Scripts\activate

- Clone or download this repository and open it in your editor of choice. 

- Then install the project dependencies with:\
  pip install -r requirements.txt

- Import the studentdata.sql file

- You need to connect to a MySQL server to run this project.\
  Edit DATABASES configurations in studentdatabase/settings.py

- Make migrations with these commands:\
  python manage.py makemigrations\
  python manage.py migrate

- Now you can run the project with this command:\
  python manage.py runserver
