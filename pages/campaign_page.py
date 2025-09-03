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
        self.page.click("//button[@aria-label='Close']")
        self.page.click("(//div[@class='campTemplate'])[1]")

    # def close_popup(self):
    #     self.page.wait_for_timeout(3000)
    #     self.page.click("//button[@aria-label='Close']")

    def select_sms_channel(self):
        self.page.click("//div[text()='SMS']")
        self.page.click("//span[text()='Customise and Send']")
        self.page.uncheck("(//input[@type='checkbox'])[3]")
        self.page.wait_for_timeout(2000)
        self.page.click(self.nextButton)

    def enter_campaign_title(self, title):
        self.page.fill(".input input[type='text']", title)
        self.page.click(self.nextButton)

    def enter_contact_phone(self):
        self.page.wait_for_timeout(2000)
        # self.page.fill(".filler", phone)
        # self.page.wait_for_timeout(2000)
        self.page.click(self.nextButton)
        self.page.wait_for_timeout(2000)
        self.page.click(self.nextButton)

    def edit_sms_content(self, message, smsmsg):
        # Locate the contenteditable div (container for SMS text)
        sms_editor = self.page.locator("//div[@class='textarea']")

        # Click inside the editor
        sms_editor.click()

        # Select all and delete existing text
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")

        # Type new message
        sms_editor.type(message)

        print(f"SMS updated to: {message}")

    def test_sms(self, phone):
        current_value = self.page.locator(self.inputField).input_value()
    
        # If the field is empty, fill it with the given phone number
        if current_value.strip() == "":
            self.page.fill(self.inputField, phone)
        
        self.page.click("button[type='submit'] span")

    def save_and_exit(self):
        self.page.click(self.saveAndExit)
