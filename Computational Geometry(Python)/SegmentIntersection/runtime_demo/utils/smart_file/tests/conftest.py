import pytest
import os

@pytest.fixture
def mock_file():
    filename = 'mock.txt'
    with open(filename, 'x') as f:
        f.write('Create a new text file!')
        yield filename
    os.remove(filename)