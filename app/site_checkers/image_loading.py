from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from app.site_checkers.base import BaseSiteChecker


class ImageLoadingSiteChecker(BaseSiteChecker):
    def __init__(self, image_xpath: str, wait_time: int = 15):
        self.image_xpath = image_xpath
        super().__init__(wait_time)

    def check_site_loaded(self, driver: webdriver.Chrome):
        wait = WebDriverWait(driver, self.wait_time)
        image_element = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, self.image_xpath)
            )
        )
        wait.until(
            lambda _: driver.execute_script(
                (
                    "return arguments[0].complete && typeof arguments[0].naturalWidth "
                    "!= 'undefined' && arguments[0].naturalWidth > 0"
                ),
                image_element,
            )
        )
