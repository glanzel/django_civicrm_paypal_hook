## Prequestits
You need an Postgresql Db up an running.
And you probably should take a look at https://github.com/HearthSim/dj-paypal/tree/main

## Install:
```
cp .env.template .env
```
Set all the variables there.
```
python3 -m pip install poetry
poetry install
poetry run python3 manage.py migrate
```

## Start:
```
poetry run gunicorn runserver
```
open a browser an go to:
```
localhost:8000/hello?name=yourname
```

to see greetings to you.
