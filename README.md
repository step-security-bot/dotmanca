# The Official Dotman Website

The Official Website for Dotman Comics

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

## Getting Ready

This describes how I'll need to set up my dev environment in a mac (what I currently use ).

You'll need the following:

- [Homebrew](https://brew.sh/)
- [Docker](https://www.docker.com/get-docker)

Next run the following:

    $ brew install pyenv

This gives you a way to manage multiple python versions at the same time.

> Note: `pyenv` is not the same as `virtualenv` or `venv`. Yay, naming!

Next, we need to install the correct Python version, and then switch to it.

    $ pyenv install 3.11
    $ pyenv global 3.11

If you just want the python version local to a particular directory, you can instead run the following inside the directory you want to run a specific version for:

    $ pyenv local 3.11

Next, we want to install Poetry. We can follow [these instructions](https://python-poetry.org/docs/).

Once Poetry is installed, we can run the following in the root of this project:

    $ poetry install

We'll also need `tox`:

    $ brew install tox

Create an `.env` file in the root of the project folder. It should contain the following items:

```
DJANGO_READ_DOT_ENV_FILE=True
POSTGRES_PASSWORD=django_pass
POSTGRES_USER=django_user
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

DJANGO_ADMIN_URL=
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=UseAGeneratedValueOrDontAsItsLocal
DJANGO_ALLOWED_HOSTS=.dotman.ca
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

USE_S3=True
AWS_S3_ENDPOINT_URL=http://localhost:9000
AWS_ACCESS_KEY_ID=minioadmin
AWS_SECRET_ACCESS_KEY=minioadmin
AWS_STORAGE_BUCKET_NAME=dotmanca
AWS_S3_REGION_NAME=
DOTMAN_STATIC_AND_MEDIA_BASE_URL=http://localhost:9000

STATIC_LOCATION=static
PUBLIC_MEDIA_LOCATION=media
```

You can review those settings, or accept as-is since this is for local. Do not use the above for production or UA environments. The `DATA_BASE_URL` must contain `POSTGRES_PASSWORD` and `POSTGRES_USER`.

Next, we can bring up the junk database to use:

    $ docker compose up postgres -d

And we'll also want a junk S3 server to use:

    $ docker compose up s3 -d

These commands only bring up a database and and S3 compatible server.

> Note: you will need to create the busket in Minio (the S3 compatible server) manually.

## Basic Commands

### Running locally

```
poetry shell
export DJANGO_READ_DOT_ENV_FILE=True
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py migrate
python manage.py runserver
```
> Note: you only need to run the `python manage.py migrate` once, but it never hurts to run again (it'll detect no new migrations, and do nothing).

### Setting Up Your Users

- To create an **superuser account**, use this command:

      $ python manage.py createsuperuser

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

```
tox run -e coverage
open htmlcov/index.html
```

#### Running tests with `pytest`

    $ tox run -e test

> Note: `pyproject.toml` has configurations for `pytest` to work.

### Lint code

This project uses `flake8` to lint code. We can run it through `tox`:

```
tox run -e lint
```

Some `flake8` configs are in the `tox.ini` file under the `flake8` heading and the `pycodestyle` heading.

### Run `black`

To run black and reformat all files:

```
tox run -e black -- .
```

To check if the files pass `black`'s formatting (use in CI pipeline):

```
tox run -e black -- --check --diff .
```

### Run `isort`

To run `isort` to sort all imports in python files:

```
tox run -e isort -- .
```

To just check that the imports are all sorted (use in a CI pipeline)

```
tox run -e isort -- --check --diff .
```