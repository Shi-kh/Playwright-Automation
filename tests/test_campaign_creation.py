import pytest
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.campaign_page import CampaignPage
from utils import config

def test_create_campaign(page):
    # Step 1 - Create Account & Login
    signup = SignupPage(page)
    signup.create_account(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD)

    login = LoginPage(page)
    login.login(config.TEST_USER_EMAIL, config.TEST_USER_PASSWORD)

    # Step 2 - Navigate to Campaigns
    dashboard = DashboardPage(page)
    dashboard.open_campaigns()

    # Step 3 - Campaign Flow
    campaign = CampaignPage(page)
    campaign.select_template()
    campaign.select_sms_channel()
    campaign.enter_campaign_title(config.CAMPAIGN_TITLE)
    campaign.enter_contact_phone(config.TEST_PHONE_NUMBER)
    campaign.edit_sms_content(config.SMS_MESSAGE)
    campaign.test_sms(config.TEST_PHONE_NUMBER)
    campaign.save_and_exit()
