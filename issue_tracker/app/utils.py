"""Common utility functions.
"""
import datetime
import random

from django.contrib.auth.models import User
from django.db import IntegrityError
from issue_tracker.app import models

USERS = (('Mike', 'Bibriglia', 'mbibrigl',),
         ('Bill', 'Cosby', 'bcosby',),
         ('John', 'Stewart', 'jstewart',),
         ('John', 'Oliver', 'joliver',),
         ('Stephen', 'Colbert', 'scolbert',),
         ('Conan', 'Obrien', 'teamcoco',),
         ('Tina', 'Fey', 'thirtyrockfey',),
         ('George', 'Carlin', 'gcarlin',),
         ('Jonny', 'Carson', 'jcarson',),
         ('George', 'Burns', 'jburns',),)

DESCRIPTIONS = (
    "Everybody let's go. Go. \nJump up, wiggle and giggle with the "
    "Mother Goose Club. \nI'm Teddy, \nI'm Eep, \nI'm Baa Baa Sheep. \n"
    "'m Mary,\nI'm Jack, \nI'm Little Bo Peep. \nEverybody let's go. Go. \n"
    "Sing a song, we'll all sing along with the Mother Goose Club. \n"
    "The Mother Goose Club.",
    "Clap your hands.\nClap your hands.\nClap them just like me.\n\n"
    "Touch your shoulders.\nTouch your shoulders.\n"
    "Touch them just like me.\n\n"
    "Pat your knees.\nPat your knees.\nPat them just like me.\n\n"
    "Stomp your feet.\nStomp your feet.\nStomp them just like me.\n\n"
    "Clap your hands.\nClap your hands.\nNow let them quiet be.\n",)

TITLES = (
    "I stole a pot.",
    "core dump on the mainframe of my dashboard.",
    "Swallowed the cat to catch the bird, swallowed the bird"
    " to catch the spider, but no spider caught",
    "Man thrown on cart claims not to be dead yet.",
    "I got an A in CS 673, but deserved an A+.",
    "But I shot a man in reno, just to watch him die.",
    "Living on a prayer, but expected to be living on a pension.",
    "Not sleeping well enough. Should sleep through night.",
    "I have fallen, and I cannot get up.",
    "Everything is broken.",
    "General. Failing. Help",
    "Another random bug.",
    "I want my bikeshed painted BLUE though!",
    )


def create_user(first, last, username, out_handle=None):
    """Create the django super user account.

    Args:
      first: First name.
      last: Last name.
      username: User handle.
      out_handle: The output handler for printing.
    """
    try:
        user = User.objects.create_user(username=username,
                                        email='%s@bu.edu' % username,
                                        password='%spw' % username,
                                        **{'first_name': first,
                                           'last_name': last})
        user.save()
    except IntegrityError:
        if out_handle:
            out_handle.write(
                'User already exists, skipping creation: %s' % username)


def create_users(users, out_handle=None):
    """Create some number of users

    Args:
      users: A tuple of tuples containing first name, last name and user.
      out_handle: The output handler for printing.
    """
    if out_handle:
        out_handle.write('\nCreating users...')
    for full_user in users:
        (first, last, username) = full_user
        create_user(first, last, username, out_handle)


def create_super_user(first, last, username, out_handle=None):
    """Create the django super user account.

    Args:
      first: First name.
      last: Last name.
      username: User handle.
      out_handle: The output handler for printing.
    """
    if out_handle:
        out_handle.write('\nCreating Super User...')
    try:
        user = User.objects.create_superuser(username,
                                             email='%s@bu.edu' % username,
                                             password='%spw' % username,
                                             **{'first_name': first,
                                                'last_name': last})
        user.save()
    except IntegrityError:
        if out_handle:
            out_handle.write('User already exists, skipping creation: %s'
                             % username)


def create_issues(number_of_issues, out_handle=None):
    """Creating some number of random issues.

    The issues will start in various states with random assignees.

    Args:
      num: The number of issues to be created.
      out_handle: The output handler for printing.
    """
    # This extra work for user ids is necessary due to the fact that the
    # database might have been wiped, but the origin pk for the user still
    # has been claimed, so we must gather the current pk list to apply them
    # to create issues.
    user_ids = []
    for user in User.objects.all():
        user_ids.append(user.pk)
    title_count = len(TITLES) - 1
    description_count = len(DESCRIPTIONS) - 1
    if out_handle:
        out_handle.write('\nCreating issues')
    for _ in xrange(number_of_issues):
        if out_handle:
            out_handle.write('.', ending='')
            out_handle.flush()
        models.Issue.objects.create(
            title=TITLES[random.randint(0, title_count)],
            description=DESCRIPTIONS[
                random.randint(0, description_count)],
            issue_type=models.TYPES[
                random.randint(1, len(models.TYPES) - 1)][0],
            status=models.STATUSES[
                random.randint(1, len(models.STATUSES) - 1)][0],
            priority=models.PRIORITIES[
                random.randint(1, len(models.PRIORITIES) - 1)][0],
            project=models.PROJECTS[
                random.randint(1, len(models.PROJECTS) - 1)][0],
            # TODO(jdarrieu): Add more randomization to this)
            modified_date=datetime.datetime.now(),
            submitted_date=datetime.datetime.now(),
            reporter=User.objects.get(
                pk=user_ids[random.randint(0, len(user_ids) - 1)]),
            )
    if out_handle:
        out_handle.write('\n')


def wipe_db():
    """This will wipe the database of all Users and Issues."""
    User.objects.all().delete()
    models.Issue.objects.all().delete()
