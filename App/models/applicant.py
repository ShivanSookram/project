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
  resume = db.Column(db.String, nullable = False)                                     #changed resume to a string - url
  registered = db.Column(db.Boolean, default=False, nullable=False)                   #added registered attribute to differentiate registered apps from non registered apps
  rejected = db.Column(db.Boolean, default=False, nullable=True)                      #added rejected attribute for placing user in rejected list
  internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'))
  internship = db.relationship('Internship', backref=db.backref('applicants', lazy=True))

  __table_args__ = (
    db.UniqueConstraint('email', 'internship_id', name='_email_internship_uc'),
  )      #unique constraint (_email_internship_uc) ensures that an applicant with the same email (emails are unique) and 
  #internship id cannot exist (ie a reapplication)! UPDATE - added phone too just in case (phone no unique also)
  #Further Update - REMOVED: adding phone illogical as applicants usually have 2+ phones and that combination would pass

  def __init__(self, first_name, last_name, email, phone, current_field_study, date_of_birth, id, resume):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone = phone
    self.current_field_study = current_field_study
    self.date_of_birth = date_of_birth
    self.resume = resume
    self.internship_id = id

  def __repr__(self):
    return f"<Applicant {self.first_name} {self.last_name}>"
