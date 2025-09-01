from playwright.sync_api import Page

class CampaignPage:
    def __init__(self, page: Page):
        self.page = page

    def select_template(self):
        self.page.click("css=.template-list .template-item:nth-child(1) button")

    def select_sms_channel(self):
        self.page.uncheck("input[name='channel_email']")
        self.page.uncheck("input[name='channel_whatsapp']")
        self.page.check("input[name='channel_sms']")

    def enter_campaign_title(self, title):
        self.page.fill("input[name='campaign_title']", title)

    def enter_contact_phone(self, phone):
        self.page.fill("input[name='contact_phone']", phone)

    def edit_sms_content(self, message):
        self.page.fill("textarea[name='sms_content']", message)

    def test_sms(self, phone):
        self.page.fill("input[name='test_phone']", phone)
        self.page.click("button:has-text('Test the campaign')")

    def save_and_exit(self):
        self.page.click("button:has-text('Save & Exit')")
