# Third Party Imports
from sqlalchemy import Column, String, Integer, TIMESTAMP, DateTime
from sqlalchemy.sql import text

# Local Application Imports
from ipt.db.base import Base 

class Customer(Base):
    __tablename__="customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(25),nullable=False)
    num_media_sent = Column(Integer, nullable=False, server_default=0)
    created_at = Column(TIMESTAMP,nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP,nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    def as_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "num_media_sent": self.num_media_sent,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
    def __repr__(self):
        return str(self.as_dict())
    
    

