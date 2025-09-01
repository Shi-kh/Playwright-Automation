import pytest
from playwright.sync_api import sync_playwright
from utils import config

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(config.BASE_URL)
    yield page
    context.close()
