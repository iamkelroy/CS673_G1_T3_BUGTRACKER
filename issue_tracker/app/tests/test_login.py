from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from django.test.testcases import LiveServerTestCase
from time import sleep
import os

class CreateIssueTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        user = User.objects.create_superuser(username="username", password="password", email="joewdriver@gmail.com")
        user.save()

    def tearDown(self):
        self.driver.quit()
        User.objects.all().delete()

    def test_create_issue(self):



        self.driver.get("localhost:8081/")
        self.driver.find_element_by_id("id_username").send_keys("username")
        self.driver.find_element_by_id("id_password").send_keys("password")
        self.driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        sleep(5)