import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture (scope = "function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=5000)
        context = browser.new_context()
        yield page
        page.close()
        browser.close()