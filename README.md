# Teaching Platform
A teaching platform system built using Django framework. It is designed for interactions between students and teachers. Features include class schedules, project selection and teacher interactions. 

## Installation

Python 3.10 and Django need to be installed.

```
$ python -m pip install -r requirements.txt
```

## Configuration

- Create the `teaching_platform_db` database
- Run the migrations: `$ python manage.py migrate`
- Create a superuser: `$ python manage.py createsuperuser`

## Usage

- Run below command

```
$ python manage.py runserver
```

 - Then click on the url to launch the platform
**http://127.0.0.1:8000/**