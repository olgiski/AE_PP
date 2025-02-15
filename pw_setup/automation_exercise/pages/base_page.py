from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self,page:Page):
        self.page = page
    def visit (self,url:str):
        self.page.goto(url)    
    def get_title(self):
        return self.page.title()
    def take_screenshot(self, filename="screenshot.png") :
        self.page.screenshot(path=f"screenshots/{filename}")   


       