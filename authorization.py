from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    login_btn = page.get_by_test_id('login-page-login-button')
    wrong_creds_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    creds_text = 'Wrong email or password'

    email_input.fill('email')
    password_input.fill('password')
    login_btn.click()

    expect(wrong_creds_alert).to_be_visible()
    expect(wrong_creds_alert).to_have_text(creds_text)

    page.wait_for_timeout(5000)