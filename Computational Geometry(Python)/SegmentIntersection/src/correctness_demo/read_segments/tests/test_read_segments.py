from src.correctness_demo.read_segments.segment_reader import SegmentReader


class TestReadSegments:
    def test_read_segments(self, mock_segments, mock_file_with_segment_data):
        assert SegmentReader().run(filename=mock_file_with_segment_data) == mock_segments
