"""This is a basic unit test file example.
These tests are to be run when 'manage.py test' is called.
"""

from django import test
from issue_tracker.app import utils
from issue_tracker.app import views
import unittest

# @unittest.skip
class SimpleViewTest(test.TestCase):

    def setUp(self):
        self.user_name = 'janedoe'
        self.user_pw = '%spw' % self.user_name
        utils.create_user(first='Jane',
                          last='Doe',
                          username=self.user_name)
        self.super_user_name = 'superuser'
        self.super_user_pw = '%spw' % self.super_user_name
        utils.create_super_user(first='Super',
                                last='Woman',
                                username=self.super_user_name)

    def testCreateIssueView(self):
        create_issue = views.CreateIssue()
        self.assertEqual('create_issue.html', create_issue.template_name)

    def testSearchView(self):
        c = test.Client()
        self.assertTrue(c.login(username=self.user_name,
                                password=self.user_pw))
        response = c.post('/issue/search/', {})
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.content)
