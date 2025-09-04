# Automation with Python Playwright

This repository contains Playwright-based end-to-end automation scripts for **Reelo (dev.reelo.io)**.  
It covers account creation, campaign setup, SMS channel configuration and test campaign execution.  

---

## Prerequisites

1. Install **Python 3.9+**  
   ```bash
   python --version
   ```

2. Install **pipenv** or use `venv` (recommended for isolated env).  
   ```bash
   pip install pipenv
   ```

3. Install project dependencies.  
   ```bash
   pipenv install
   ```

   Or if using `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```

4. Install **Playwright** + required browsers.  
   ```bash
   pip install playwright pytest pytest-playwright
   playwright install
   ```

---

## Project Structure

```
reelo-automation/
│── README.md
│── conftest.py                  # Pytest fixtures
│── tests/
│   └── test_create_campaign.py   # Main automation test
│── pages/
│   ├── signup_page.py            # Page Object for Sign Up
│   ├── campaign_page.py          # Page Object for Campaigns
│   └── sms_page.py               # Page Object for SMS steps
│── utils/
│   └── config.py                 # Config vars (numbers, creds)
```

---

## Environment Variables

Create a `.env` file (never commit this!) with:  

```ini
REELO_BASE_URL=https://dev.reelo.io
REELO_EMAIL=testuser@example.com
REELO_PASSWORD=YourPassword123
MOBILE_NUMBER=+1XXXYYYZZZZ

---

## Running the Tests

1. Run **pytest** (default headless mode):  
   ```bash
   pytest -v tests/
   ```

2. Run in **headed mode** (visible browser):  
   ```bash
   pytest -v tests/ --headed
   ```

3. Run with **parallel workers**:  
   ```bash
   pytest -n auto
   ```

## Example Test Flow

1. **Sign Up / Create Account**  
   - Fill full name, email, password, mobile number.  
   - Enter OTP (dummy / Twilio).  

2. **Campaign Creation**  
   - Select campaign template.  
   - Choose SMS channel.  
   - Enter campaign title.  
   - Enter terms with your number.  
   - Customize SMS text (insert your name).  
   - Upload logo/banner.  

3. **Trigger Test Campaign**  
   - Send test SMS to your number.  
   - Validate SMS received.  

---

## Debugging

- Run Playwright in slow mode:  
  ```bash
  pytest -v tests/ --headed --slowmo 500
  ```

- Capture trace logs:  
  ```bash
  pytest -v tests/ --tracing on
  ```

- Debug selectors in inspector:  
  ```bash
  playwright codegen https://dev.reelo.io
  ```

---

With this setup, you can **create accounts, handle OTPs, configure campaigns, and test SMS delivery automatically**.
