from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


#Using: https://demoqa.com/buttons
class DoubleClickPage(BasePage):
    DOUBLE_BTN = (By.ID, "doubleClickBtn")
    DOUBLE_MSG = (By.ID, "doubleClickMessage")

    def double_click_button(self):
        button = self.find(self.DOUBLE_BTN)
        ActionChains(self.driver).double_click(button).perform()

    def get_double_click_message(self):
        return self.find(self.DOUBLE_MSG).text
