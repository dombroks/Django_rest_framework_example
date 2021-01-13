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
