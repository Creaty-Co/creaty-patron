from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver


class BaseSiteChecker(ABC):
    def __init__(self, wait_time: int = 15):
        self.wait_time = wait_time

    def check_site_loaded(self, driver: WebDriver):
        raise NotImplementedError
