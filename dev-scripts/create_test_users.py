"""Script for populating test users.

THIS SCRIPT IS FOR DEVELOPMENT PURPOSES ONLY.

To run:
        python manage.py shell < create_test_users.py
"""
from django.contrib.auth.models import User
from django.db import IntegrityError
from issue_tracker import settings


def CreateUsers():
    if settings.DEBUG:
        print '\nCreating users...'
        users = ['jdarrieu',
                 'jwansman',
                 'driverj',
                 'atohuang',
                 'sameran',
                 'tedseng',
                 'tsaoyl91',
                 'danazh']
        for user in users:
            try:
                u = User.objects.create_user(user, email='%s@bu.edu' % user,
                                             password='%spw' % user)
                u.save()
            except IntegrityError:
                print 'User already exists, skipping creation: %s' % user


def CreateSuperUser():
    if settings.DEBUG:
        print '\nCreating Super User...'
        superuser = 'test'
        try:
            u = User.objects.create_superuser(superuser,
                                              email='%s@bu.edu' % superuser,
                                              password='%spw' % superuser)
            u.save()
        except IntegrityError:
            print 'User already exists, skipping creation: %s' % superuser

CreateUsers()
CreateSuperUser()
