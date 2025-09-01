from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = "input[id='email']"
        self.password_input = "input[id='password']"
        self.signup_button = "button[type='submit']"
        self.fullName = "input[id='name']"
        self.mobile_signup = "input[id='number']"


    def create_account(self, email, password):
        self.page.click("text=Sign up")
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.signup_button)
