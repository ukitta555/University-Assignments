from typing import TextIO
from unittest.mock import patch

from interface import implements  # type: ignore

from runtime_demo.utils.smart_file.callback_that_uses_file import CallbackThatUsesFile
from runtime_demo.utils.smart_file.smart_file import SmartFile


@patch("test_smart_file.CallbackThatUsesFile")
class TestSmartFile:
    def test_callback_execution(self, mock_callback, mock_file):
        instance = mock_callback.return_value
        instance.run.return_value = 42
        return_value = SmartFile(mock_file).do_something_using_file(CallbackThatUsesFile())
        assert len(instance.run.mock_calls) == 1
        assert return_value == 42

    def test_is_file_closed(self, mock_file):
        file = SmartFile(mock_file)
        assert file.is_file_opened is False
        file.do_something_using_file(CallbackThatUsesFile())
        assert file.is_file_opened is False
