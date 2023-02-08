from sqlalchemy.ext.declarative import declarative_base
from .db import db
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from typing import List, Union
from pydantic import BaseModel
from sqlalchemy.orm import Session

Base = declarative_base()

class CompanyModel(Base):
    __tablename__ = "companies"
    company_id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255))
    description= Column(String(255))
    country = Column(String(255))
    founding_date = Column(String(255))
    deals = relationship("DealModel", back_populates="cmpny")


class DealModel(Base):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"))
    date = Column(String(255))
    funding_amount = Column(String(255))
    funding_round = Column(String(255))
    cmpny = relationship("CompanyModel", back_populates="deals")

# class Company(BaseModel):
#     company_id: int
#     name: str
#     description: str
#     country:str
#     founding_date:str

#     class Config:
#         orm_mode = True


# class Deal(BaseModel):
#     id: int
#     company_id: int
#     date: str
#     funding_amount: str
#     funding_round: str
    
#     class Config:
#         orm_mode = True

# def get_companies(db: Session,skip : int=0,limit:int = 1000):
#     return db.query(CompanyModel).offset(skip).limit(limit).all()

# def get_deals(db: Session,skip : int=0,limit:int = 1000):
#     return db.query(DealsModel).offset(skip).limit(limit).all()

#  def create_company(db: Session, company: Company):
#     db_company = Company(company_id=Company.company_id,name= Company.name,
#         description=Company.description,country=Company.country,founding_date=Company.founding_date)
#     db.add(db_company)
#     db.commit()
#     db.refresh(db_company)
#     return db_company

#  def create_deal(db: Session, company: Deal):
#     db_deal = Deal(company_id=Deal.company_id,date= Deal.date,
#         funding_amount=Deal.funding_amount,funding_round=Deal.funding_round)
#     db.add(db_deal)
#     db.commit()
#     db.refresh(db_deal)
#     return db_deal   