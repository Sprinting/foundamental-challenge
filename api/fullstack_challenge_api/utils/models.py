from sqlalchemy.ext.declarative import declarative_base
from .db import db
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description= Column(String)
    country = Column(String)
    founding_date = Column(DateTime)

    deals = relationship("Deals", back_populates="cmpny")


class Item(Base):
    __tablename__ = "items"

    company_id = Column(Integer, ForeignKey("companies.id"))
    date = Column(DateTime)
    funding_amount = Column(Integer, index=True)
    funding_round = Column(String)
    cmpny = relationship("Company", back_populates="deals")
 