from playwright.sync_api import Playwright
from pages.base_page import BasePage

class EnterAccountInfo:
    def __init__(self, page:Page):
        super().__init__(page)
        self.title_mrs = "input#id_gender2"
        self.name = "#name"
        self.email = "#email"
        self.password = "#password"
        self.select_day = "select#days"
        self.select_month = "select#months"
        self.select_year = "select#years"
        self.newsletter = "#newsletter"
        self.offers = "#optin"
        self.first_name = "#first_name"
        self.last_name = "#last_name"
        self.company = "#company"
        self.address1 = "#address1"
        self.address2 = "#address2"
        self.country = "select#country"
        self.state = "#state"
        self.city = "#city"
        self.zipcode = "#zipcode"
        self.mobile_number = "#mobile_number"
        self.create_account_button = "//button[contains(text(),'Create')]"
