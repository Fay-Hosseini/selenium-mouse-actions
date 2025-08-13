from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

"""Using: https://demoqa.com/slider"""
class SlidePage(BasePage):
    SLIDER = (By.CLASS_NAME, "range-slider")
    SLIDER_VALUE = (By.ID, "sliderValue")

    def move_slider(self, offset):
        slider = self.find(self.SLIDER)
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(offset, 0).release().perform()
        slider_value = int(self.find(self.SLIDER_VALUE).get_attribute("value"))
        print(f"Slider value after move: {slider_value}")  # <-- print here
        assert slider_value > 50, f"Slider value did not increase, current: {slider_value}"
        assert slider_value == int(slider.get_attribute("value"))
        return slider_value
