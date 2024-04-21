from App.models.applicant import Applicant
from App.database import db


def create_applicant(first_name, last_name, email, phone, current_field_study, date_of_birth, resume, int_id):
  newapplicant = Applicant(first_name=first_name, last_name=last_name, email=email, phone=phone,
                           current_field_study=current_field_study, date_of_birth=date_of_birth, resume=resume, id=int_id)
  db.session.add(newapplicant)
  db.session.commit()
  return newapplicant
