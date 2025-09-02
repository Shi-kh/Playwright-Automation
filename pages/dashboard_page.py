from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def open_campaigns(self):
        self.page.click("//span[text()='Campaigns']")


