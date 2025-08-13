from pages.double_click_page import DoubleClickPage

def test_double_click(driver):
    page = DoubleClickPage(driver)
    page.open("https://demoqa.com/buttons")
    page.double_click_button()
    message = page.get_double_click_message()
    assert message == "You have done a double click", f"Unexpected message: {message}"