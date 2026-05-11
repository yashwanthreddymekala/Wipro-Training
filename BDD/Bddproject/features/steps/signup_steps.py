import allure
from behave import given, when, then

from pages.signup_page import SignUpPage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

logger=LogGen.loggen()

@given(u'User launches Demoblaze application')
def step_impl(context):
    logger.info('demoblaze url loaded')

@when(u'User clicks on Sign up menu')
def step_impl(context):
    logger.info("Step : Click Sign Up Menu")
    context.signup_page=SignUpPage(context.driver)
    context.signup_page.click_signup_menu()

@when(u'User enters signup username "useraaaaa"')
def step_impl(context,username):
    logger.info(f"Step : Enter UserName : {username}")
    context.signup_page.enter_username(username)


@when(u'User enters signup password "pwdaaaaa"')
def step_impl(context,password):
    logger.info(f"Step : Enter UserName : {password}")
    context.signup_page.enter_password(password)


@when(u'User clicks Signup button')
def step_impl(context):
    logger.info(f"Step : Click Sign UP button")
    context.signup_page.click_signup_button()


@then(u'User should see signup success message')
def step_impl(context):
    logger.info("Step : Verify Successful Sign up Message")
    context.login_page.verify_successful_signup()
    screenshot_path = (ScreenshotUtil.capture_screenshot(context.driver, "successful_signup"))
    logger.info(f"Screenshot Captured : {screenshot_path}")
    allure.attach(context.driver.get_screenshot_as_png(), name="Successful SignUp",
                  attachment_type=allure.attachment_type.PNG)
