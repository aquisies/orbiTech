from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    firstname = Column(String(100))
    lastname = Column(String(100))
    phone = Column(String(20))
    website = Column(String(255))
    estado_clickup = Column(String(20))

class CallRecord(Base):
    __tablename__ = 'call_records'

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    params = Column(String(255))
    result = Column(String(255))

class APICall(Base):
    __tablename__ = 'api_calls'

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    params = Column(String(255))
    result = Column(String(255))
