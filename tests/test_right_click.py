from pages.right_click_page import RightClickPage

def test_right_click(driver):
    page = RightClickPage(driver)
    page.open("https://demoqa.com/buttons")
    page.right_click_button()

    message = page.get_right_click_message()
    assert message == "You have done a right click", f"Unexpected message: {message}"
