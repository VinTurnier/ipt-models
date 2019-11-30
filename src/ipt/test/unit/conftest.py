# Third Party Imports
import pytest

# Local Application Imports
from ipt.db_factories import ImageFactory, CustomerFactory
from ipt.db import Image, Customer, session

@pytest.fixture(scope='function')
def image_factory():
    return ImageFactory.build()

@pytest.fixture(scope='function')
def customer_factory():
    return CustomerFactory.build()

@pytest.fixture(scope='module')
def ipt_session():
    return session