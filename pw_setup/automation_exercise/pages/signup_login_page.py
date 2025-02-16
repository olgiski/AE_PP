from playwright.sync_api import Playwright
from pages.base_page import BasePage
from playwright.sync_api import Page


class SignupLoginPage:
    def __init__(self,page: Page):
        super().__init__(page)
        self.new_user_signup_title = "//h2[contains(text(),'Signup')]"
        self.new_user_name_input = "//input[@name = 'name']"
        self.new_user_email_input = "//input[@data-qa= 'signup-email']"
        self.signup_button = "//button[contains(text(),'Signup')]"
