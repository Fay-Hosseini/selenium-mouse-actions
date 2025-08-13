from pages.scroll_page import ScrollPage

def test_scroll(driver):
    page= ScrollPage(driver)
    page.open("https://demoqa.com")
    page.scroll_to_button()
