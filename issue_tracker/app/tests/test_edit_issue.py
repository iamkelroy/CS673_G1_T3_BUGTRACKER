from selenium.webdriver.common.keys import Keys
from app.tests import base_testcase


class CreateIssueTestCase(base_testcase.CommonLiveServerTestCase):

    def test_view_issue(self):

        # For this to work we need to either run a script to create generic
        # issues, or create an issue to view as part of the test.  Currently
        # creating dynamically, but there's a better way to do this when we
        # have time using mocks or a script

        self.driver.get('localhost:8081/issue/create')
        self.driver.find_element_by_id(
            'id_username').send_keys(self.super_user_name)
        self.driver.find_element_by_id(
            'id_password').send_keys(self.super_user_pw)
        self.driver.find_element_by_id('id_password').send_keys(Keys.ENTER)
        self.pause()
        self.driver.find_element_by_xpath(
            '//*[@id="id_project"]/option[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="id_issue_type"]/option[2]').click()
        self.driver.find_element_by_id('id_title').send_keys('Sample Title')
        self.driver.find_element_by_id('id_description').send_keys(
            'Luke, I am your father')
        self.driver.find_element_by_xpath(
            '//*[@id="id_priority"]/option[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="id_assignee"]/option[2]').click()
        self.driver.find_element_by_css_selector(
            '.btn-primary[value="Create"]').click()

        # save a value
        title = self.driver.find_element_by_class_name('bug_name').text
        # click on edit issue.
        self.driver.find_element_by_css_selector(
            '#main-menu > li:nth-child(4) > a:nth-child(1)').click()
        # edit a value
        self.driver.find_element_by_id('id_title').send_keys('blarg')
        # save changes
        self.driver.find_element_by_css_selector('.btn-primary')
        # check value changed
        self.assertNotEqual(
            title,
            self.driver.find_element_by_class_name('bug_name').text)
