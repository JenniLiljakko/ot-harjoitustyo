import pytest
from database import start_test



@pytest.fixture(scope="session", autouse=True)
def start_test_db():
    start_test()
