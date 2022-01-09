from runtime_demo.utils.smart_file.callback_that_uses_file import CallbackThatUsesFile


class SmartFile:
    def __init__(self, filename):
        self.filename: str = filename
        self.file_handler = None
        self.is_file_opened = False

    def do_something_using_file(self, callback: CallbackThatUsesFile = None, **kwargs):
        if not callback:
            raise ValueError("Please provide a callback to do something with opened file!")

        self._open_file_()
        result = callback.run(file_handler=self.file_handler, **kwargs)
        self._close_file_()
        return result

    def _open_file_(self):
        if self.is_file_opened:
            return

        self.file_handler = open(self.filename, "r")
        self.is_file_opened = True

    def _close_file_(self):
        if not self.is_file_opened:
            return

        self.file_handler.close()
        self.file_handler = None
        self.is_file_opened = False

