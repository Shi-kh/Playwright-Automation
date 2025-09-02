from playwright.sync_api import Page

class CampaignPage:
    def __init__(self, page: Page):
        self.page = page
        self.nextButton = "button[type='submit']"
        self.smsInput = "input[placeholder='Select Store Name']"
        self.inputField = "input[type='number']"
        self.saveAndExit = "(//button[@class='primary-btn'])[1]"

    def select_template(self):
        self.page.click("//h5[text()= ' Navratri Specials (22nd Sept - 1st Oct)']")
        self.page.click("(//div[@class='campTemplate'])[1]")

    def close_popup(self):
        self.page.click("//button[text()='Close']")

    def select_sms_channel(self):
        self.page.click("//div[text()='SMS']")
        self.page.click("//span[text()='Customise and Send']")
        self.page.uncheck("(//input[@type='checkbox'])[3]")
        self.nextButton.click()

    def enter_campaign_title(self, title):
        self.page.fill(".input input[type='text']", title)
        self.nextButton.click()

    def enter_contact_phone(self, phone):
        self.page.fill(".filler", phone)
        self.nextButton.click()

    def edit_sms_content(self, message):
        self.page.fill(smsInput, " ")
        self.page.fill(smsInput, message)
        self.nextButton.click()

    def test_sms(self, phone):
        current_value = self.page.locator(inputField).input_value()
    
        # If the field is empty, fill it with the given phone number
        if current_value.strip() == "":
            self.page.fill(inputField, phone)
        
        self.page.click("button[type='submit'] span")

    def save_and_exit(self):
        self.saveAndExit.click()
