import sys
import os
from typing import cast

from SeleniumLibrary import SeleniumLibrary
from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert

from libraries.logger import LogGen
from libraries.screenshot_util import ScreenshotUtil

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from robot.api.deco import keyword
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from robot.libraries.BuiltIn import BuiltIn

from resources.locators.login_locators import (
    LOGIN_LINK,
    USERNAME_TEXTBOX,
    PASSWORD_TEXTBOX,
    LOGIN_BUTTON,
    WELCOME_USER
)

from resources.variables.config import config

from resources.variables.testdata import (
    VALID_USERNAME,
    VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
)

logger=LogGen.loggen()
class LoginPage:

    def __init__(self):
        self.selenium = cast(
            SeleniumLibrary,
            BuiltIn().get_library_instance(
                "SeleniumLibrary"
            ))

    @keyword
    def launch_demoblaze_application(self):
        logger.info('Opening browser')
        self.selenium.open_browser(
            config.base_url,
            browser=config.browser
        )
        self.selenium.maximize_browser_window()
        self.selenium.set_selenium_implicit_wait(
            config.implicit_wait
        )

    @keyword
    def click_login_link(self):
        logger.info('Clicking Login')
        self.selenium.click_element(
            LOGIN_LINK
        )

    @keyword
    def enter_username(self):
        logger.info('Entering Username')
        self.selenium.input_text(
            USERNAME_TEXTBOX,
            VALID_USERNAME
        )

    @keyword
    def enter_password(self):
        logger.info('Entering password')
        self.selenium.input_text(
            PASSWORD_TEXTBOX,
            VALID_PASSWORD
        )

    @keyword
    def click_signin_button(self):
        logger.info('Clicking Sign in button')
        self.selenium.click_button(
            LOGIN_BUTTON
        )

    @keyword
    def verify_successful_login(self):
        logger.info('Verifying successful login')
        WebDriverWait(
            self.selenium.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                (By.ID, "nameofuser")
            )
        )
        welcome_text = self.selenium.get_text(
            WELCOME_USER
        )
        print(welcome_text)
        assert "Welcome" in welcome_text

    # ================INVALID=====================

    @keyword
    def enter_invalid_login_username(self):
        logger.info('Entering Invalid username')
        self.selenium.input_text(
            USERNAME_TEXTBOX,
            INVALID_USERNAME
        )

    @keyword
    def enter_invalid_login_password(self):
        logger.info('Entering invalid password')
        self.selenium.input_text(
            PASSWORD_TEXTBOX,
            INVALID_PASSWORD
        )

    @keyword
    def validate_invalid_login_alert(self):
        logger.info('validating invalid success alert')
        try:
            WebDriverWait(
                self.selenium.driver,
                10
            ).until(
                EC.alert_is_present()
            )
            alert = Alert(self.selenium.driver)
            logger.info(f'Alert text:{alert.text}')
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'login_success')
            alert.accept()
        except TimeoutException:
            logger.info('Login Success alert timeout')
            ScreenshotUtil.capture_screenshot(self.selenium.driver, 'login_success_timeout')
            raise AssertionError(
                "Invalid login alert not displayed"
            )