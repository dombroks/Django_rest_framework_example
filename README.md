# Django_rest_framework_example

In this projet I created an API using python-based django rest framework, I used Mysql as database.

In order to make things work perfectly you need to follow this guide:

## Installation

### Virtual Environment

    $sudo apt install python3-venv python3-pip
    $python3 -m venv “/path to your location folder”

### Activate the virtual environment

   $source <location folder>/bin/activate
  
### Install latest django version
  
    $pip install django

    $pip install djangorestframework

### Start django project and app.

    $django-admin startproject core

    $ cd core

    $python manage.py startapp employeeApp

### Connecte Django with MySQL DB

    $mysql -u 'root' <  "employees.sql" -p

### Switch the Django default Database from sqlite3 to MySQL

You can do that by replacing the default DATABASES section with this:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'employees',
            'USER': 'root',
            'PASSWORD':'password',
            'HOST':'0.0.0.0',
            'PORT':''
        }
    }

### Generating the models according to the database (if the db has exicting data)

    $pip install mysqlclient
    $python manage.py inspectdb > employeeApp/models.py

### Make migrations then migrate

    $python manage.py makemigrations
    $python manage.py migrate

### Add employeeApp & restframeword in INSTALLED_APPS (settings.py)

    INSTALLED_APPS = [    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employeesApp',
    'rest_framework',]

- You'll will the rest of what you need in the code

Note: To test the code, all what you need to do is running the server by this command:

    $python manage.py runserver 0.0.0.0:8080

and opening your browser and entering the url http://127.0.0.1:8080/api
