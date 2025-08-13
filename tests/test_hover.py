from pages.hover_page import HoverPage

def test_hover(driver):
    page = HoverPage(driver)
    page.open("https://the-internet.herokuapp.com/hovers")
    page.hover_over_first_image()