from runtime_demo.utils.smart_file.callback_that_uses_file import CallbackThatUsesFile


class SmartFile:
    def __init__(self, filename):
        self.filename: str = filename
        self.file_handler = None
        self.is_file_opened = False

    def do_something_using_file(self, callback: CallbackThatUsesFile = None, **kwargs):
        if not callback:
            raise ValueError("Please provide a callback to do something with opened file!")

        self.__open_file__()
        result = callback.run(file_handler=self.file_handler, **kwargs)
        self.__close_file__()
        return result

    def __open_file__(self):
        if self.is_file_opened:
            return

        self.file_handler = open(self.filename, "r")
        self.is_file_opened = True

    def __close_file__(self):
        if not self.is_file_opened:
            return

        self.file_handler.close()
        self.file_handler = None
        self.is_file_opened = False

