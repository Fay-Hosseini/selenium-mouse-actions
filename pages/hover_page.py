from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

    #Using: https://the-internet.herokuapp.com/hovers
class HoverPage(BasePage):
    IMAGE = (By.XPATH, "(//img[@alt='User Avatar'])")

    def hover_over_first_image(self):
        element = self.find_all(self.IMAGE)[0]
        ActionChains(self.driver).move_to_element(element).perform()

