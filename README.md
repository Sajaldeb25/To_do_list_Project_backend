# To Do List Backend Project
# 📖 
A To-Do list is a list that you can keep to put all of the tasks that you need to complete on a given day. It can be very useful for managing time, by planning your day ahead of time, and prioritizing activities. This project helps you ta accomplish simple to-do management task. 

# 📋 Setup

It is best to use the python `virtualenv` tool to build locally:
- Clone the repository

```shell script
$ git clone https://github.com/Sajaldeb25/To_do_list_Project_backend.git
$ cd To_do_list_Project_backend
```
- Create Virtual environment and Install dependencies

```diff
$ virtualenv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

- Make `.env` file to the root directory of the project. `.env` file should contains following variables.
```
SECRET_KEY=
ALLOWED_HOSTS=
DEBUG=
SQLITE_URL=
CORS_ALLOWED_ORIGINS=
```

# 📋 Run
```shell script
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Then visit [http://localhost:8000/todos_get/](http://localhost:8000) to view backend of the app.

# 📋 APIs of the App

- `Get` todo list
- `Update` a specific todo 
- `Delete` a specific todo
- `Post/create` a todo 



# 📋 Folder Structure 
```
To_do_list_project_backend
├── todoapp
│    ├── migrations                           - migration file, which contains all migration history. 
│                  ├── __init__.py            - Initial migration
│                  ├── 0001_initial.py        - First migration 
│    
│    ├── admin.py     
│    ├── __init__.py  
│    ├── admin.py
│    ├── apps.py
│    ├── models.py              - It contains Task model 
│    ├── serializer.py          - Serialize model data 
│    ├── tests.py
│    ├── urls.py                - Defines path for urls
│    ├── views.py
├── todoproject
│    ├── __init__.py
│    ├── settings.py            - Contains setting of the project, including REST-Api, Database connection, and app name. 
│    ├── urls.py
│    ├── wsgi.py
│    ├── asgi.py
│── .gitignore
│── manage.py                    
│── requirements.txt             - requirements file for install configuration  

```


