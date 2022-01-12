from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
from selenium.webdriver.firefox.options import Options
import os

# Open the browser and go to selected URL
class UIFlow():

    def browserOpens(self,uri):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(uri)
    
    def pictureSnapped(self):
        self.driver.save_screenshot('./static/images/screenshots.png')
        print("Screenshot taken")

if __name__ == '__main__':
    ui = UIFlow()
    ui.browserOpens(uri='https://facebook.com')
    ui.pictureSnapped()