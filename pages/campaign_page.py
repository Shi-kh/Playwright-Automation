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

    def select_sms_channel(self):
        self.page.click("//div[text()='SMS']")
        self.page.click("//span[text()='Customise and Send']")
        self.page.uncheck("(//input[@type='checkbox'])[3]")
        self.page.wait_for_timeout(2000)
        self.page.click(self.nextButton)

    def enter_campaign_title(self, title):
        self.page.fill(".input input[type='text']", title)
        self.page.wait_for_timeout(2000)
        self.page.click(self.nextButton)

    def enter_contact_phone(self):
        self.page.wait_for_timeout(2000)
        self.page.click(self.nextButton)

    def upload_logo(self, image_path: str):
        file_input = self.page.locator(".upload-btn")
        self.page.wait_for_timeout(2000)
        # Attach the file
        file_input.set_input_files(image_path)
        self.page.click("//span[text()='Save']")
        self.page.click(self.nextButton)

    def edit_sms_content(self, first_text, second_text):
        spans = self.page.locator("//div[@class='textarea']//span[@contenteditable='true']")
        count = spans.count()
        self.page.wait_for_timeout(2000)

        # Clear first field
        spans.nth(0).click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        spans.nth(0).type(first_text)

        # Clear second span
        spans.nth(1).click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        spans.nth(1).type(second_text)
        self.page.click(self.nextButton)

    def test_sms(self, phone):
        current_value = self.page.locator(self.inputField).input_value()
    
        # If the field is empty, fill it with the given phone number
        if current_value.strip() == "":
            self.page.fill(self.inputField, phone)
        
        self.page.click("button[type='submit'] span")

    def save_and_exit(self):
        self.page.click(self.saveAndExit)
