# Django tutorial

## Create a virtual enviroment
Before starting, create a virtual enviroment

`mkdir project_name`

`cd project_name`

`python -m venv .`

### Django
- Install django
`pip install django`

- Check installation `import django
django.VERSION`

### Create new project
- Go to the root directory where you are going to create the project

`cd root_dir`

`django-admin startproject project_name . `

### Create new App
Apps are django's way to modulerize a project, inside an app you can have multiple Model-View-Template components.

`cd project_name`

`python manage.py startapp app_name`

Every time you create a new `app`, rememeber to add it to settings.py `INSTALLED_APPS` and you can check if app is registered ok with `python manage.py check app_name`

## Optional dependencies
Every time a framework-related dependency is installed, rememeber to add it to settings.py `INSTALLED_APPS`

### SLL webserver
- SSL in development environment
`pip install django-sslserver`

- check server
`python manage.py runsslserver 0.0.0.0:8888`

### Crispy Forms
- Instal crispy forms
`pip install django-crispy-forms`


## Start coding
This is not a complete django course, it is just a template to remind you the django's features. 

Django is based on an architecture-design-pattern Model-View-Template (_MVT_) similar to Model-View-Controller (_MVC_) with some concepts switched.

### Models

_MVT Model_ equivalent to _MVC Model_

Defined in `models.py`. Contains the core-business-domain logic and the core data entities, this is the deepest layer and in theory the code here can be reused with minimal modifications on other frameworks.

Obviously the _data entities_ if a different ORM is used on other framework, it has to be addapted but the core-business-domain python logic should remain untouch.

Even this is the deepest layer and it is related to _data entities_ do not include database implementation here, always use the desing pattern _repository_ to make the databases interchangeable.

#### Migrations

Remember to properly configure your database credentials before.

Once you define them, every time a change is made you need to create the _migrations_ and run them to create or upload the database schema.


- Migration definition, this is where the python is 'translated' to SQL.

`python manage.py makemigrations`

- Migration update, this is where the SQL is sent to the database.

To sent a specific migration `python manage.py sqlmigrate app_name migration_number`

Or

To run all migrations `python manage.py migrate`

### Views
_MVT View_ equivalent to _MVC Controller_ .Yes it is weird and unintuitive but that's the way it is.

This is the architectural component that makes the comunication between _Models_ and _Templates_

No core-business-domain logic should be placed here, just framework-related logic.

### Templates
The _MVT Template_ equivalent  _MVC Views_. Once again concepts switched.

These are the HTML Templates with a built-in tags language to incluide dynamic data.

### Routing
Django uses server-side rendering, meaning that the HTML is sent to the browser by the server everytime a request is made to a _route_ (URL) 

There are ways to sent data such as JSON objects, instead of HTML, with custom javascript, but django normall behaviour is to render HTML with dynamic data already embedded everytime a request is made.

You need to correctly set up the routing to hit the views
Remember to register urls in:

- app_name/urls.py
- project_name/urls.py

The request flow goes like this:

1. Client _request_ hits a _Route
2. _Route_ calls a _View_
3. _View_ calls _Models_ to retrieve database data if necessary.
4. _Models_ requests data to the database
5. The database returns data to the _Model_
6. The _Models_ returns data to the _View_
7. The _View_ receives the data, executes logic if necessary, embbeds the data into the _Template_ and renders the _Template_
8. The _Template_ is sent to the browser.


### Buil-in CRUD - Admin panel
Django has an admin panel to interact with _Models_ and the database directly without the need of coding a custom CRUD. 

You can have multiple _Models_ but maybe you'll want to do CRUD operations with some of them, not all. If you want to, register in `admin.py` the model classes you want to interact.

#### Superuser interactive creation
To login you will need a super-user.
`python manage.py createsuperuser`

Save these credentials in a secure place.

Once you are in with this super-user you can create all the users you want, grant permissions, etc.

#### Superuser programmatic creation
In your dev enviroment you got your super-user but remember that when you do a deploy in a PaaS service for the first time, the database schema is created from scratch and will not have any data in it, inclusing the users data.

The first time you do a deploy you'll need to create a super-user in the prod environment or even the test environment in case you have one.

You can do this using the terminal in the remote server.

Some PaaS free services doesn't provide you with a terminal, in that case you'll need to create a super-user as part of the deploy process, *but only the first time you deploy*, not on each deploy.

Use enviroment variables on the prod server to set the super-user credentials, remember that you will change this after the app is deployed for the first time.


``DJANGO_SUPERUSER_USERNAME=admin``

``DJANGO_SUPERUSER_EMAIL=email@xxx.com``

``DJANGO_SUPERUSER_PASSWORD=first_password``

## Run the server

- Regular server
`python manage.py runserver`

- SSL server
`python manage.py runsslserver`

## Deploy

You'll need to follow the instruction on the service you want to deploy. Some of the tasks you'll need to do considering a PaaS service:

- Set up enviroment variables manually using the admin panel
- Set up github action deploy workflow using the github-PaaS integration feature.

As part of the deploy process, maybe you will have to execute some scripts after the deploy is made:

This is a sample ``build.sh`` script file for the **Render PaaS** to execute after your deploy is done, to configurations automatically on each deploy.

```
#!/usr/bin/env bash

# exit on error

set -o errexit

# Upgrade pip

/opt/render/project/src/.venv/bin/python3.11 -m pip install --upgrade pip

# Install the dependencies, these are part of the git repo requirements.txt deployed 

pip install -r requirements.txt

# Collect all static files from your apps and any other places defined in your settings into a single location that can be served by a web server

python manage.py collectstatic --no-input

# Sent migrations to the database

python manage.py migrate

# Create a super-user only if it does not exists in the database

python manage.py createsuperuser_if_none_exists --user=user_name --password=first_password --email=superusert@savingl.cl`

