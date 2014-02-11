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
    local('python ./manage.py runserver')

@task
@runs_once
def delpyc():
    """
    Runs the local Django server
    """
    local('find . -name "*.pyc" -delete')

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
    # local("rm ")


# @task
# @runs_once
# def test(what="all"):
#     """
#     Execute all tests.
#     """
#     print "test"
#     # command = 'ssh emmasocial -tt "source .virtualenvs/emmasocial/bin/activate; cd emmasocial/src; sudo python manage.py test {what}"'.format(what=("emmasocial" if what == "all" else what))
#     # tests = dict(
#     #     emmasocial="cd {base_dir}vm/ && {command}".format(base_dir=BASE_DIR, command=command),
#     #     couchdb='cd {base_dir} && grunt test:couchdb'.format(base_dir=BASE_DIR),
#     #     client='cd {base_dir} && grunt test:client'.format(base_dir=BASE_DIR),
#     # )

#     # # run all tests (except functional)
#     # if what == "all":
#     #     for which in tests:
#     #         local(tests[which])


# @task
# @runs_once
# def migrate():
#     """
#     Runs migratedb commands
#     """
#     print "migrate"
#     # local("")
