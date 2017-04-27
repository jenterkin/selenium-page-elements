from .fixtures.page_objects import page_object


class TestInputField:
    def test_input_get(self, page_object):
        assert page_object.input_field == ''

    def test_input_set(self, page_object):
        new_value = 'test string'
        page_object.input_field = new_value
        assert page_object.input_field == new_value
        page_object.driver.get_screenshot_as_file('/tmp/input.png')


class TestTextArea:
    def test_textarea_get(self, page_object):
        assert page_object.textarea == ''

    def test_textarea_set(self, page_object):
        new_value = 'test string'
        page_object.textarea = new_value
        page_object.textarea == new_value
        page_object.driver.get_screenshot_as_file('/tmp/textarea.png')


class TestSelectBox:
    def test_selectbox_get(self, page_object):
        assert page_object.select_box == 'first'

    def test_selectbox_set(self, page_object):
        page_object.select_box = 'second'
        assert page_object.select_box == 'second'
        page_object.driver.get_screenshot_as_file('/tmp/selectbox.png')


class TestCheckBox:
    def test_checkbox_get(self, page_object):
        assert page_object.checkbox == False

    def test_checkbox_set(self, page_object):
        page_object.checkbox = True
        assert page_object.checkbox == True
        page_object.driver.get_screenshot_as_file('/tmp/checkbox.png')
