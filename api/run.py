from fullstack_challenge_api.utils import models
from fullstack_challenge_api.utils import db
engine = db.db.engine
models.Base.metadata.create_all(bind=engine)

# with open("../data/companies.csv") as companies:
#     session = db.db.sessionmaker()
#     for company in companies:
#         name,country,founding_date,description,company_id = company.split("|||") 
#         cmpny = models.CompanyModel(
#             company_id= int(company_id),
#             name = name,
#             description= description,
#             country = country,
#             founding_date = founding_date
#         )
#         session.add(cmpny)
#         session.commit()
#         session.refresh(cmpny)
#         session.close()

with open("../data/deals.csv") as deals:
    session = db.db.sessionmaker()
    for deal in deals:
        date,funding_amount,funding_round,company_id = deal.split("|||") 
        _deal = models.DealModel(
            date= date,
            funding_amount = funding_amount,
            funding_round = funding_round,
            company_id = int(company_id)
        )
        if(session.get(models.CompanyModel,company_id) is not None):
            session.add(_deal)
            session.commit()
            session.refresh(_deal)
        session.close()