from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, DateField, FileField, SubmitField, validators
from App.models import db, Applicant 

form_views = Blueprint('form_views', __name__, template_folder='../templates')

@form_views.route('/submit', methods=['POST'])
def create_applicant():
    data = request.form
    flash(f"Applicant {data['first_name']} added!")
    create_applicant(data['first_name'],data['last_name'],data['telephone'],data['email'],data['current_field_study'],data['first_name'],data['date_of_birth'], data['resume'])
    return redirect('index.html')

