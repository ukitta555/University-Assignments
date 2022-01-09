from runtime_demo.correctness_demo.read_segments.read_segments import ReadSegments
from runtime_demo.utils.smart_file.smart_file import SmartFile


class TestReadSegments:
    def test_read_segments(self, mock_segments, mock_file_with_mock_segment_data):
        segments = SmartFile(mock_file_with_mock_segment_data)\
            .do_something_using_file(ReadSegments())
        assert segments == mock_segments
