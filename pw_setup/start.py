from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.automationexercise.com/")
        print(page.title)
        title = "Automation Exercise"
        assert title in page.title()
        browser.close()