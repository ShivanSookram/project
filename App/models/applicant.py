from wtforms import FileField
from App.database import db

class Applicant(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False)
  phone = db.Column(db.String, nullable=False)
  current_field_study = db.Column(db.String, nullable=False)
  date_of_birth = db.Column(db.String, nullable=False)
  resume = FileField('Resume')
  internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=False)
  internship = db.relationship('Internship', backref=db.backref('applicants', lazy=True))

  def __init__(self, first_name, last_name, email, phone, current_field_study, date_of_birth, resume, id):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone = phone
    self.current_field_study = current_field_study
    self.date_of_birth = date_of_birth
    self.resume = resume
    self.internship_id =  id

  def __repr__(self):
    return f"<Applicant {self.first_name} {self.last_name}>"
