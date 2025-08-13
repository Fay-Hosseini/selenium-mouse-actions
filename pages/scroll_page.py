from pages.base_page import BasePage

"""Using: https://demoqa.com"""
class ScrollPage(BasePage):
    def scroll_to_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")