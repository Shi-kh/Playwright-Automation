from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = "input[id='email']"
        self.password_input = "input[id='password']"
        self.signup_button = "button[type='submit']"
        self.fullName = "input[id='name']"
        self.mobile_signup = "input[id='number']"
        self.country_code = "button[type='button']"
        self.country_US = "(//span[text()='+1'])[1]"

    def create_account(self, fullName,email, mobile_signup, password):
        self.page.click("//span[text()='Sign up']")
        self.page.fill(self.fullName, fullName)
        self.page.fill(self.email_input, email)

        # Select country code as US
        self.page.click(self.country_code)
        self.page.click(self.country_US)

        # Re-click mobile field to bring focus back
        mobile_field = self.page.locator(self.mobile_signup)
        mobile_field.click()
        mobile_field.type(mobile_signup, delay=100)  

        # Fill password
        self.page.fill(self.password_input, password)

        # Submit form
        self.page.click(self.signup_button)
        self.page.wait_for_timeout(5000)
        self.page.wait_for_event("load")

