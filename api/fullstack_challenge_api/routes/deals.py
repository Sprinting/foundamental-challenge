from fastapi import APIRouter, Depends
from fullstack_challenge_api.utils.db import get_db
from fullstack_challenge_api.utils import models
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/deals")
async def get_companies(db: Session = Depends(get_db)):
    return models.get_deals(db=db)
