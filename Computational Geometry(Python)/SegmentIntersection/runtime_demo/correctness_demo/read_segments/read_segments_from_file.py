from runtime_demo.correctness_demo.read_segments.read_segments\
    import ReadSegments
from runtime_demo.utils.smart_file.smart_file import SmartFile

def read_segments_from_file():
    small_example_filename = "small_example.txt"
    result = SmartFile(small_example_filename) \
        .do_something_using_file(ReadSegments())
    return result
