import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)


class Patient(Base):
    __tablename__ = "Patient"

    id          = Column(Integer, primary_key=True, index=True)
    ktp         = Column(Integer, unique=True)
    full_name   = Column(String, nullable=False) # = first_name + last_name
    first_name  = Column(String, nullable=False)
    last_name   = Column(String, default='')
    address     = Column(Text, nullable=False)
    
    # disease = relationship('Disease', secondary=Patient_Disease, backref='Patient')
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True, nullable=False)

    def default_values(self):
        response = dict()
        response['id']          = self.id
        response['ktp']         = self.ktp
        response['full_name']   = self.full_name
        response['first_name']  = self.first_name
        response['last_name']   = self.last_name
        response['address']     = self.address
        response['created_date']    = self.created_date.isoformat() if self.created_date else None
        response['modified_date']   = self.modified_date.isoformat() if self.modified_date else None
        response['is_active']       = self.is_active

        return response
