from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage

"""Using: https://demoqa.com/buttons"""
class RightClickPage(BasePage):
    RIGHT_BTN =(By.ID, "rightClickBtn")
    RIGHT_MSG = (By.ID, "rightClickMessage")

    def right_click_button(self):
        button = self.find(self.RIGHT_BTN)
        ActionChains(self.driver).context_click(button).perform()

    def get_right_click_message(self):
        return  self.find(self.RIGHT_MSG).text

