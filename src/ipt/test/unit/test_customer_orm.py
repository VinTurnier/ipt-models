# Third Party Imports
import pytest

# Local Application Imports
from ipt.db import Customer

def test_insert_customer(customer_factory,ipt_session):
    customer = Customer(phone_number=customer_factory.phone_number,
                        num_media_sent=customer_factory.num_media_sent,
                        created_at=customer_factory.created_at,
                        updated_at = customer_factory.updated_at)
    ipt_session.add(customer)
    ipt_session.commit()
    customer = ipt_session.query(Customer).filter_by(phone_number=customer_factory.phone_number).first()
    assert customer.phone_number == customer_factory.phone_number

def test_as_dict_return_value(ipt_session):
    customer = ipt_session.query(Customer).first()
    result = customer._asdict()
    assert isinstance(result,dict)
    assert 'id' in result
    assert 'phone_number' in result
    assert 'num_media_sent' in result
    assert 'created_at' in result
    assert 'updated_at' in result


def test_representation(ipt_session):
    customer = ipt_session.query(Customer).first()
    result = str(customer)
    assert isinstance(result,str)
    assert 'id' in result