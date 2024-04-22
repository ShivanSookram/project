from App.models import db
from App.models import internship
from App.models.internship import Internship
from sqlalchemy.exc import IntegrityError


def create_internship(internship_title,company_name,location,start_date,stipend,duration):
  new_internship = Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,stipend=stipend,duration=duration)
  try:
    db.session.add(new_internship)
    db.session.commit()
    
  except IntegrityError:
    db.session.rollback()
    new_internship = None
    
  return new_internship
