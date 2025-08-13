from pages.slider_page import SlidePage

def test_slider(driver):
    page = SlidePage(driver)
    page.open("https://demoqa.com/slider")
    page.move_slider(15)
