import pytest
from pages.home_page import HomePage
from utils import config

def test_home_page(page):
    homepage = HomePage(page)
    homepage.visit(config.BASE_URL)
    homepage.validate_title("Automation Exercise")
    homepage.signup_login_button()