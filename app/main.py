import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app.site_checkers.base import BaseSiteChecker
from app.site_checkers.image_loading import ImageLoadingSiteChecker


class Patron:
    def __init__(self, url: str, checker: BaseSiteChecker):
        self.url = url
        self.checker = checker
        self.driver = self.create_driver()

    def create_driver(self) -> webdriver.Chrome:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('--incognito')
        return webdriver.Chrome(options=options)

    def load_site(self):
        self.driver.get(self.url)

    def run(self, interval: int = 2):
        try:
            while True:
                self.load_site()
                self.checker.check_site_loaded(self.driver)
                time.sleep(interval)
        finally:
            self.driver.close()
            self.driver.quit()


def main():
    URL = 'https://dev.creaty.club'
    IMAGE_PATH = (
        '/html/body/div/main/div/div[3]/div/div[2]/div/div/div/div[14]/div/div/div[1]/'
        'img'
    )
    checker = ImageLoadingSiteChecker(IMAGE_PATH)
    patron = Patron(URL, checker)
    patron.run()


if __name__ == '__main__':
    main()
