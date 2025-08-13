from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

"""Using: https://demoqa.com/droppable"""
class DragDropPage(BasePage):
    SOURCE = (By.ID, "draggable")
    TARGET = (By.ID, "droppable")

    def drag_and_drop(self):
        src = self.find(self.SOURCE)
        tgt = self.find(self.TARGET)
        ActionChains(self.driver).drag_and_drop(src,tgt).perform()

    def get_drop_text(self):
        return self.find(self.TARGET).text

