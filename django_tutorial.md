# Django tutorial

## Create a virtual enviroment
Before starting, create a virtual enviroment

## Instalations
### Django
- Install django
`pip install django==4.1`

- Check installation and django version on interactive console
`import django
django.VERSION`

### SLL webserver
- SSL in development environment
`pip install django-sslserver`

- include sslserver in settings.py > installed apps

- run server
`python manage.py runsslserver 0.0.0.0:8888`

### Django-environ
- Install and configure django-environ
`pip install django-environ`
Follow django-environ documentation to set up or sample projects to get along with the configuration-


### Crispy Forms
- Instal crispy forms
`pip install django-crispy-forms`

- Add crispy_forms to your INSTALLED_APPS in settings.py

`INSTALLED_APPS = (
    ...
    'crispy_forms',
)`

## Comands
### Create new project
- Go to the root directory where you are going to create the project

`cd rootDir`

`django-admin startproject projectname`

- Set up .gitignore.
There is a boilerplate in ml_querier project, include .env, *.ipynb, *.txt and other files you want to exclude from git versioning.

### Create new App

`cd projectDir`

`python manage.py startapp appName`

- Register new app in settings.py

- Check if app is registered ok

`python manage.py check appName`

- Write the view functions.

- Write the html templates

- Register url's in:
appDir/urls.py and update projectDir/urls.py


### Create models and database
- Write the models in models.py if necessary.
- Run the migrations

`python manage.py makemigrations`

`python manage.py sqlmigrate appName migrationNumber`
Or
`python manage.py migrate`

- Register in admin.py the model classes to be able to use de admin panel to interact with the tables.

### Run the server

- Regular server
`python manage.py runserver`

- SSL server
`python manage.py runsslserver`

### Manage admin panel

- Create superuser
`python manage.py createsuperuser`

- Create superuser non-interactively


1. Open cmd terminal
Watch all enviroment variables to see if already exist the ones we need.

``set``

2. Set or overwrite enviroment variables

``set DJANGO_SUPERUSER_USERNAME=admin``

``set DJANGO_SUPERUSER_EMAIL=email@xxx.com``

``set DJANGO_SUPERUSER_EMAIL=emailrandom524@gmail.com``

3. Run 
``manage.py createsuperuser --noinput``


If you need to clear an enviroment variable run

``set ENVIROMENT_VARIABLE=``

To manipulate enviroment variables using python

``import os``

get environment variables

``os.getenv('ENVIROMEN_VARIABLE')``

print all enviroment variables

``print(os.environ)``



