from runtime_demo.correctness_demo.read_segments.read_segments_from_file import ReadSegments


class TestReadSegments:
    def test_read_segments(self, mock_segments, mock_file_with_segment_data):
        assert ReadSegments().run(filename=mock_file_with_segment_data) == mock_segments
