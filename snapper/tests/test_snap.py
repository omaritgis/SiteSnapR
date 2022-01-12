from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import unittest

# Path: snapper/tests/test_snap.py
# Open the browser and go to selected URL
class UIFlow(unittest.TestCase):

    def test_browserOpens(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://google.com")
    
    def test_pictureSnapped(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://google.com")
        self.driver.save_screenshot('test_screenshot.png')
        screenshot = Image.open('test_screenshot.png')
        screenshot.show()

if __name__ == '__main__':
    ui = UIFlow()
    ui.test_browserOpens()
    ui.test_pictureSnapped()