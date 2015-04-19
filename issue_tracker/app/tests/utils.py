from selenium.webdriver.common.keys import Keys


class SearchPage():
    search_button = ".btn-primary"
    search_title = "#id_title"


class Sidebar():
    search_button = "#main-menu > li:nth-child(6) > a:nth-child(1)"


class Dashboard():
    top_issue = ".sortable > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)"


class ViewIssue():
    issue_title = "#page-inner > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > p:nth-child(1) > b:nth-child(1)"


class Issue_Builder():
    def __init__(self, webdriver):
        self.driver = webdriver

    def create_issue(self, title="Sample", description="Description"):
        self.driver.find_element_by_xpath(
            '//*[@id="id_project"]/option[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="id_issue_type"]/option[2]').click()
        self.driver.find_element_by_id('id_title').send_keys(title)
        self.driver.find_element_by_id('id_description').send_keys(
           description)
        self.driver.find_element_by_xpath(
            '//*[@id="id_priority"]/option[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="id_assignee"]/option[2]').click()
        self.driver.find_element_by_css_selector(
            '.btn-primary[value="Create"]').click()

    def login(self, username, password):
        self.driver.find_element_by_id('id_username').send_keys(username)
        self.driver.find_element_by_id('id_password').send_keys(password)
        self.driver.find_element_by_id('id_password').send_keys(Keys.ENTER)