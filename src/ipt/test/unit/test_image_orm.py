# Third Party Imports
import pytest 

# Local Application Imports
from ipt.db import Image 

def test_insert_new_image(image_factory, ipt_session):
    img = image_factory
    image = Image(url=img.url,num_of_matches=img.num_of_matches)
    ipt_session.add(image)
    ipt_session.commit()
    inserted_image = ipt_session.query(Image).filter_by(url=img.url).first()
    assert inserted_image.url == img.url

def test_as_dict_return_value(ipt_session):
    img = ipt_session.query(Image).first()
    result = img._asdict()
    assert isinstance(result,dict)
    assert 'url' in result
    assert 'id' in result
    assert 'num_of_matches' in result
    assert 'timestamp' in result

def test_representation(ipt_session):
    img = ipt_session.query(Image).first()
    result = str(img)
    assert isinstance(result,str)



