from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self,page:Page):
        super().__init__(page)
        self.title = "//title[contains(text(),'Automation Exercise')]"
        self.home_button = "//a[contains(text(),'Home')]"
        self.signup_login_button = "//a[contains(text(),'Signup')]"
        self.cart_button = "//a[contains(text(),'Cart')]"
        self.contact_us_button = "//a[contains(text(),'Contact')]"

    def validate_title(self,expected_title):
        #self.expected_title = expected_title
        actual_title = self.page.title()  # ✅ Call the method correctly
        assert actual_title == expected_title, f"Expected '{self.expected_title}', but got '{actual_title}'"

    def click_signup_login(self):
        self.page.locator(self.signup_login_button).click() 

