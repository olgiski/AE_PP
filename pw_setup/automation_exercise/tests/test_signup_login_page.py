import pytest
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from utils import config

def test_signup (page):
    homepage = HomePage(page)
    homepage.visit(config.BASE_URL)
    homepage.click_signup_login()
    signup_page = SignupLoginPage(page)
    signup_page.verify_signup()
    signup_page.signup()
