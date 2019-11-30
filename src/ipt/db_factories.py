# Standard Library Imports
import datetime

# Third Party Imports
import factory
import factory.fuzzy


# Local Application Imports
from ipt.db import Image, Customer

class ImageFactory(factory.alchemy.SQLAlchemyModelFactory):
     
     id = factory.Sequence(lambda n: n)
     url = factory.Faker('hostname')
     num_of_matches = factory.fuzzy.FuzzyInteger(0,30,1)
     timestamp = datetime.datetime.now()

     class Meta:
         model = Image
         sqlalchemy_session_persistence = 'commit'

class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):

    id = id = factory.Sequence(lambda n: n)
    phone_number = factory.Faker('phone_number')
    num_media_sent = factory.fuzzy.FuzzyInteger(2,30,1)
    created_at = datetime.datetime.now() + datetime.timedelta(-30)
    updated_at = datetime.datetime.now()

    class Meta:
        model = Customer
        sqlalchemy_session_persistence = 'commit'
