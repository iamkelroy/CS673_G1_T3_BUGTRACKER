from selenium.webdriver.common.keys import Keys
from app.tests import base_testcase
from utils import SearchPage, Dashboard, Issue_Builder, ViewIssue
import time


class ViewIssueTestCase(base_testcase.CommonLiveServerTestCase):

    def test_view_issue(self):
        # for this to work we need to either run a script to create generic
        # issues, or create an issue to view as part of the test.  Currently
        # creating dynamically, but there's a better way to do this when we
        # have time using mocks or a script

        self.driver.get('localhost:8081/issue/create')
        builder = Issue_Builder(self.driver)
        builder.login(self.super_user_name, self.super_user_pw)
        self.pause()
        builder.create_issue("Sample Title")
        assert self.driver.find_element_by_css_selector(ViewIssue.issue_title).text == "Title: Sample Title"

        # The above code just creates an issue, the following is where
        # our test begins
        time.sleep(5)
        self.driver.find_element_by_css_selector("#main-menu > li:nth-child(6) > a:nth-child(1)").click()
        self.pause()
        self.driver.find_element_by_css_selector(SearchPage.search_title).send_keys('Sample Title')
        self.driver.find_element_by_css_selector(SearchPage.search_button).click()
        self.driver.find_element_by_css_selector(Dashboard.top_issue).click()
        time.sleep(5)
        assert self.driver.find_element_by_css_selector(ViewIssue.issue_title).text == "Title: Sample Title"
        self.pause()
