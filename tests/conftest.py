import pytest
import os


@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def resources(rootdir):
    return os.path.join(rootdir, 'resources')
