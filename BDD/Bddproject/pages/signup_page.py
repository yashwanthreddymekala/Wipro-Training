import allure
import self

from locators.signup_locators import SignUpLocators
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil
from utils.waits import WaitUtils

logger=LogGen.loggen()

class SignUpPage:
    def __init__(self,driver):
        self.driver=driver

    def click_signup_menu(self):
        logger.info("clicking login menu")
        WaitUtils.wait_for_element_clickable(self.driver,SignUpLocators.SIGNUP_MENU).click()

    def enter_username(self, username):
        logger.info(
            f"Entering Username : {username}"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            SignUpLocators.USERNAME_INPUT
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        logger.info("Entering Password")
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            SignUpLocators.PASSWORD_INPUT
        )
        element.clear()
        element.send_keys(password)

    def verify_successful_signup(self):
        logger.info("Verifying signup alert")
        alert=WaitUtils.wait_for_alert(self.driver)
        
    logger.info(
        "Verifying Login Alert"
    )
    alert = WaitUtils.wait_for_alert(
        self.driver
    )
    alert_text = alert.text
    logger.info(
        f"Alert Message : {alert_text}"
    )
    ScreenshotUtil.capture_screenshot(
        self.driver,
        "signup_alert"
    )
    allure.attach(
        self.driver.get_screenshot_as_png(),
        name="signup Alert Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    alert.accept()
    return alert_text