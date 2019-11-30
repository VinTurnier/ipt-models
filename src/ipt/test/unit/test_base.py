# Third Party Imports
import pytest 

# Local Application Imports
from ipt.db_orm import base  

@pytest.mark.test_orm_base
def test_get_connection_string():
    with pytest.raises(Exception) as exec_value:
        assert base.get_connection_string(None)
    assert 'cannot be Null' in str(exec_value.value)

@pytest.mark.test_orm_base
def test_base_exports():
    assert base.session
    assert base.Base
    assert base.session.close() is None 
