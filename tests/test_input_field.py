from .fixtures.page_objects import page_object


class TestInputField:
    def test_input_get(self, page_object):
        assert page_object.input_field.value() == ''

    def test_input_set(self, page_object):
        new_value = 'test string'
        page_object.input_field = new_value
        assert page_object.input_field.value() == new_value


class TestTextArea:
    def test_textarea_get(self, page_object):
        assert page_object.textarea.value() == ''

    def test_textarea_set(self, page_object):
        new_value = 'test string'
        page_object.textarea = new_value
        assert page_object.textarea.value() == new_value


class TestSelectBox:
    def test_selectbox_get(self, page_object):
        assert page_object.select_box.value() == 'first'

    def test_selectbox_set(self, page_object):
        page_object.select_box = 'second'
        assert page_object.select_box.value() == 'second'


class TestCheckBox:
    def test_checkbox_get(self, page_object):
        assert page_object.checkbox.value() == False

    def test_checkbox_set(self, page_object):
        page_object.checkbox = True
        assert page_object.checkbox.value() == True
