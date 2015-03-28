from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
from django.test.testcases import LiveServerTestCase
from time import sleep
import os

class TestSideBar(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        user = User.objects.create_superuser(username="username", password="password", email="tester@test.com")
        user.save()

    def tearDown(self):
        self.driver.quit()
        User.objects.all().delete()

    def test_sidebar(self):

        self.driver.get("localhost:8081/issue/create")
        self.driver.find_element_by_id("id_username").send_keys("username")
        self.driver.find_element_by_id("id_password").send_keys("password")
        self.driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@href="/"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@href="/admin/login/"]').click()
        sleep(3)
        # Currently, the admin site changes to django admin site. This has no
        # links to point back to the originating page.
        self.driver.get("localhost:8081/")
        self.driver.find_element_by_xpath('//*[@href="/issue/create"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@href="/"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@href="/issue/search"]').click()
        sleep(3)
       
        

     
       
       
