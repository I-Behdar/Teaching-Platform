# Teaching Platform
A teaching platform system built using Django framework. It is designed for interactions between students and teachers. Features include class schedules, project selection and teacher interactions. 

## Installation

Python 3.10 and Django need to be installed.

```
$ python -m pip install -r requirements.txt
```

## Configuration

Setup a PostgreSQL server and create the `teaching_platform_db` database

Run the migrations: 
```bash
python manage.py migrate
```

You might load data for development
```bash
python manage.py loaddata fixtures/users
```

Make `.env` file from `.env.template`

Create a superuser: 
```bash
python manage.py createsuperuser
```

## Usage
```
$ python manage.py runserver
```

Launch the platform at
**http://127.0.0.1:8000/**