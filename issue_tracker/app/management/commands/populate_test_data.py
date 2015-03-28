"""Script for populating test users.

THIS SCRIPT IS FOR DEVELOPMENT PURPOSES ONLY.

To run:
        python manage.py populate_test_data
"""
import datetime
import optparse
import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from issue_tracker.app import models
from issue_tracker.app import utils

class Command(BaseCommand):
    """A command for populating the database with test data/users."""

    option_list = BaseCommand.option_list + (
        optparse.make_option(
            '--issues', action='store', type='int',
            dest='issues', default=1000,
            help='The number of random issues to populate the db with.'),
        )

    def handle(self, *args, **options):
        """Where the command magic happens."""
        utils.create_users(users=utils.USERS, out_handle=self.stdout)
        utils.create_super_user(first='Super', last='Woman',
                                username='test', out_handle=self.stdout)
        utils.create_issues(number_of_issues=options['issues'],
                            out_handle=self.stdout)
