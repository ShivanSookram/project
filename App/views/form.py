from flask import Flask, render_template, redirect, url_for, request, current_app, Blueprint, flash
from wtforms import Form, StringField, TelField, EmailField, DateField, FileField, SubmitField, validators, HiddenField
import re, os
from App.models import db
from App.models import applicant
from App.models.applicant import Applicant

form_views = Blueprint('form_views', __name__, template_folder='../templates')

class ApplicationForm(Form):
  name = StringField('First Name', validators=[validators.DataRequired()])
  last_name = StringField('Last Name', validators=[validators.DataRequired()])
  telephone = TelField('Telephone', validators=[validators.DataRequired()])
  email = EmailField('Email', validators=[validators.DataRequired()])
  date_of_birth = DateField('Date of Birth', validators=[validators.DataRequired()])
  current_field_of_study = StringField('Current Field of Study', validators=[validators.DataRequired()])
  resume = StringField('Resume Link', validators=[validators.DataRequired()])
  submit = SubmitField('Submit Application')
  internship_id = HiddenField('Internship ID')
def sanitize_filename(filename):
  sanitized_filename = re.sub(r'[^\w\.-]', '_', filename, flags=re.UNICODE)
  return sanitized_filename

# @form_views.route('/form/<id>', methods=['GET'])
# def formrt(id):
#   form=ApplicationForm(request.form)
#   return render_template('form.html',id=id, form=form)

@form_views.route('/submit', methods=['GET', 'POST'])
def apply():
  form = ApplicationForm(request.form)
  if request.method == 'POST':
    if form.validate():
      name = form.name.data
      last_name = form.last_name.data
      telephone = form.telephone.data
      email = form.email.data
      date_of_birth = form.date_of_birth.data
      current_field_of_study = form.current_field_of_study.data
      resume = form.resume.data
      internship_id = form.internship_id.data
      new_applicant = Applicant(first_name=name,last_name=last_name,email=email,phone=telephone,current_field_study=current_field_of_study,date_of_birth=date_of_birth,resume=resume,int_id=internship_id)#this is to be added to the controller for this class, this is just here for testing atm
      if new_applicant:
        flash(f'Application submitted successfully! Name: {name}')
      else:
        flash(f'Error in signing up - User already applied! Name: {name}')
      flash(f'Application submitted successfully! Name: {name}')
      return redirect(url_for('index_views.index_page'))
    else:
      flash('Application not filled out. Please correct the following fields:')
      for field, errors in form.errors.items():
        for error in errors:
          flash(f'{field}: {error}')
      flash(f'field {form.internship_id.data} is filled')
      return redirect(request.referrer)

  return render_template('form.html', form=form)
