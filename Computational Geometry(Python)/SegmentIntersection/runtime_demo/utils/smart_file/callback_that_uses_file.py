from typing import Any, TextIO
from interface import Interface  # type: ignore


class CallbackThatUsesFile(Interface):
    def run(self, file_handler: TextIO = None, **kwargs) -> Any:
        pass



