# Third Party Imports
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import text 

from ipt.db.base import Base

class Image(Base):
    __tablename__='images'

    id = Column(Integer,primary_key=True,autoincrement=True)
    url = Column(String(255),nullable=False)
    timestamp = Column(DateTime,server_default=text('CURRENT_TIMESTAMP'),nullable=False)

    def _asdict(self):
        return {
            'id':self.id,
            'url':self.url,
            'timestamp':self.timestamp
        }
    
    def __repr__(self):
        return str(self._asdict())