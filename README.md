
# Django-Heroku

A django framework that develop to fit Heoku's deployment.

This is customized and developed from Python-getting-started package (cloned from https://github.com/heroku/python-getting-started.git) 

## New features

### Upgraded: Python 3.8.5, Django 3.1, Bootstrap v4.5, a new venv.
### New third-party apps: Ckeditor, 
### New apps added: Blog, authentication, tag ect.

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
