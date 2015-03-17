from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from django.test.testcases import LiveServerTestCase
import unittest
from time import sleep


class CreateIssueTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        user = User.objects.create_superuser(username="username", password="password", email="tester@gtest.com")
        user.save()

    def tearDown(self):
        self.driver.quit()
        User.objects.all().delete()

    def test_create_issue(self):

        self.driver.get("localhost:8081/issue/create")
        self.driver.find_element_by_id("id_username").send_keys("username")
        self.driver.find_element_by_id("id_password").send_keys("password")
        self.driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="id_project"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="id_issue_type"]/option[2]').click()
        self.driver.find_element_by_id("id_title").send_keys("Sample Title")
        self.driver.find_element_by_id("id_description").send_keys("Luke, I am your father")
        self.driver.find_element_by_xpath('//*[@id="id_priority"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="id_assignee"]/option[2]').click()
        self.driver.find_element_by_css_selector('.btn-primary[value="Create"]').click()
        sleep(2)
        assert "http://localhost:8081/issue/view/1/" == self.driver.current_url

    def test_create_issue_validation(self):
        self.driver.get("localhost:8081/issue/create")
        self.driver.find_element_by_id("id_username").send_keys("username")
        self.driver.find_element_by_id("id_password").send_keys("password")
        self.driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="id_project"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="id_issue_type"]/option[2]').click()
        self.driver.find_element_by_id("id_description").send_keys("Luke, I am your father")
        self.driver.find_element_by_xpath('//*[@id="id_priority"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="id_assignee"]/option[2]').click()
        self.driver.find_element_by_css_selector('.btn-primary[value="Create"]').click()
        assert self.driver.find_element_by_class_name("errorlist").is_displayed()