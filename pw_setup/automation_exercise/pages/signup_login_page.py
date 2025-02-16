from pages.home_page import HomePage
from playwright.sync_api import Page


class SignupLoginPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.new_user_signup_title = "//h2[contains(text(),'Signup')]"
        self.new_user_name_input = "//input[@name = 'name']"
        self.new_user_email_input = "//input[@data-qa= 'signup-email']"
        self.signup_button = "//button[contains(text(),'Signup')]"
    
    def home_page_methods(self):
        self.validate_title("Automation Exercise")
        self.click_signup_login()
    
    def verify_signup (self):
        is_visible = self.page.locator(self.new_user_signup_title).is_visible()
        assert is_visible, "Sign up title is not visible"
    def signup (self):
        self.page.locator(self.new_user_name_input).fill("CleoTest")
        self.page.locator(self.new_user_email_input).fill("cleo_test1@gmail.com")
        self.page.locator(self.signup_button).click()



