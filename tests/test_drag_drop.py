from pages.drag_drop_page import DragDropPage

def test_drag_drop(driver):
    page = DragDropPage(driver)
    page.open("https://demoqa.com/droppable")
    page.drag_and_drop()
    drop_text = page.get_drop_text()
    assert drop_text == "Dropped!", f"Drag and drop failed, got message: {drop_text}"