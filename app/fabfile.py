import os

from fabric.api import local, task
from fabric.decorators import runs_once

BASE_DIR = os.path.sep.join((os.path.dirname(__file__), ''))

@task
@runs_once
def runserver():
    """
    Runs the local Django server
    """
    local('open "http://127.0.0.1:8000" && python ./manage.py runserver')

@task
@runs_once
def delpyc():
    """
    Runs the local Django server
    """
    local('find . -name "*.pyc" -delete')

@task
@runs_once
def shell():
    """
    Opens a Django shell on the target environment.
    """
    local('python manage.py shell')

@task
@runs_once
def provision():
    """
    Runs the local Django server
    """
    local("pip install -r requirements.txt")

@task
@runs_once
def syncdb():
    """
    Runs the local Django server
    """
    local("python manage.py syncdb")
