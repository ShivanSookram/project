from flask import Flask, render_template, redirect, url_for, request, current_app, Blueprint, flash
from wtforms import Form, StringField, TelField, EmailField, DateField, FileField, SubmitField, validators, HiddenField
from sqlalchemy.exc import IntegrityError   #added
import re, os
from App.models import db
from App.models import internship
from App.models.internship import Internship

company_views = Blueprint('company_views', __name__, template_folder='../templates')

class CompanyForm(Form):
  internship_title = StringField(validators=[validators.DataRequired()])
  company_name = StringField(validators=[validators.DataRequired()])
  location = StringField(validators=[validators.DataRequired()])
  stipend = StringField(validators=[validators.DataRequired()])
  start_date = StringField(validators=[validators.DataRequired()])
  duration = StringField(validators=[validators.DataRequired()])
  
  #email = EmailField('Email', validators=[validators.DataRequired()])  - We WOULD need to add one in the future for contact!
  
  submit = SubmitField('Submit Application')



@company_views.route('/companyapply', methods=['GET','POST'])
def companyApply():
  form = CompanyForm(request.form)
  if request.method == 'POST':
    if form.validate():
      internship_title = form.internship_title.data
      company_name = form.company_name.data
      location = form.location.data
      #email = form.email.data
      stipend = form.stipend.data
      start_date = form.start_date.data
      duration = form.duration.data

      new_internship = Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,stipend=stipend,duration=duration)
      try:
        db.session.add(new_internship)
        db.session.commit()
        flash(f'Internship Added! Name: {internship_title}')
      except IntegrityError:
        db.session.rollback()
        flash(f'Error in adding - Internship Exists! Name: {internship_title}')
        # return redirect(request.referrer)
      # if new_applicant:
      #   flash(f'Application submitted successfully! Name: {name}')
      # else:
      #   flash(f'Error in signing up - User already applied! Name: {name}')
      # flash(f'Application submitted successfully! Name: {name}')
      return redirect(url_for('index_views.index_page'))
    else:
      flash('Application not filled out. Please correct the following fields:')
      for field, errors in form.errors.items():
        for error in errors:
          flash(f'{field}: {error}')
      return redirect(request.referrer)

  return render_template('company.html', form=form)

