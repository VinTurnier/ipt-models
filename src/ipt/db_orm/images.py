# Third Party Imports
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import text 

from ipt.db_orm.base import Base

class Image(Base):
    __tablename__='images'

    id = Column(Integer,primary_key=True,autoincrement=True)
    url = Column(String(255),nullable=False)
    key_points = Column(String(255), nullable=False)
    descriptor = Column(String(255), nullable=False)
    num_of_matches = Column(Integer, nullable=False)
    timestamp = Column(DateTime,server_default=text('CURRENT_TIMESTAMP'),nullable=False)


    def _asdict(self):
        return {
            'id':self.id,
            'url':self.url,
            'timestamp':self.timestamp,
            'num_of_matches': self.num_of_matches
        }
    
    def __repr__(self):
        return str(self._asdict())

