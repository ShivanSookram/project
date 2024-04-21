from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies, get_jwt_identity, create_access_token

from.index import index_views
from App.controllers import auth


from App.models import db, Internship, User
from App.models.applicant import Applicant

from App.controllers import (
    login
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')


'''
Page/Action Routes
'''    
@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@auth_views.route('/form/<id>', methods=['GET'])   #here
@jwt_required()
def form_page(id):
    internship = Internship.query.filter_by(id = id).first()      #here
    return render_template('form.html', title="Form",internship = internship, message=f"You are logged in as {current_user.id} - {current_user.username}")


@auth_views.route('/admin')
@jwt_required()
def admin_page():
    # Retrieve user ID from JWT
    current_user_id = get_jwt_identity() # user_identity_lookup()

    print("CURRENT USER ID = " + str(current_user_id))

    # Check if user ID is valid (optional, for extra security)
    if not current_user_id:
        return jsonify({'message': 'Unauthorized access'}), 401

    # Retrieve user data (assuming you have a function to fetch by ID)
    user_data = User.query.filter_by(id=current_user_id).first() #get_user_data(current_user_id)  # Replace with your function

    #Retrieve applicant data for rendering in admin.html

    #Create example applicant

    # newapplicant = Applicant("Billy","Ben","123-4567","applicatn@email.com","Computer Science", "01/01/1999", "resume.png", 1)
    # newapplicant1 = Applicant("Bicky","Ben","123-4567","applicatn@email.com","Computer Science", "01/01/1999", "resume.png", 1)
    # newapplicant2 = Applicant("Silly","Ben","123-4567","applicatn@email.com","Computer Science", "01/01/1999", "resume.png", 1)
    # newapplicant3 = Applicant("Stilly","Ben","123-4567","applicatn@email.com","Computer Science", "01/01/1999", "resume.png", 1)
    # newapplicant4 = Applicant("Chili","Ben","123-4567","applicatn@email.com","Computer Science", "01/01/1999", "resume.png", 1)

    # db.session.add(newapplicant)
    # db.session.add(newapplicant1)
    # db.session.add(newapplicant2)
    # db.session.add(newapplicant3)
    # db.session.add(newapplicant4)
    # db.session.commit()

    applicant_data = Applicant.query.all()

    # Render template or return JSON based on authorization
    if current_user_id == 1 or current_user_id == 2:  # Assuming admin ID is 1 (change if needed)
        return render_template('admin.html', user_data=user_data, applicant_data=applicant_data)
    else:
        return render_template ('401.html')
        
@auth_views.route('/addapplicant/<applicant_id>', methods=['GET'])
def add_applicant(applicant_id):

    print("APPLICANT ID: " + applicant_id)
    #Retrieve applicant data

    applicant = Applicant.query.filter_by(id=applicant_id).first()

    #Change applicants registered status to true

    applicant.registered = True
    db.session.add(applicant)
    db.session.commit()

    print("APPLICANT REGISTERED STATUS: " + str(applicant.registered))

    return redirect(url_for('auth_views.admin_page'))
    
@auth_views.route('/rejectapplicant/<applicant_id>', methods=['GET'])
def reject_applicant(applicant_id):

    print("APPLICANT ID: " + applicant_id)
    #Retrieve applicant data

    applicant = Applicant.query.filter_by(id=applicant_id).first()

    #Change applicants registered status to true

    applicant.rejected = True
    db.session.add(applicant)
    db.session.commit()

    print("APPLICANT REJECTED STATUS: " + str(applicant.rejected))

    return redirect(url_for('auth_views.admin_page'))

#Login And sign up pages

@auth_views.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@auth_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password'])
    response = redirect(request.referrer)
    if not token:
        flash('Bad username or password given'), 401
    else:
        flash('Login Successful')
        response = redirect(url_for('index_views.home_page')) #set response to redirect to home page if successful
        set_access_cookies(response, token) 
    return response

#signup route

@auth_views.route('/signup', methods=['POST'])
def signup_action():

  data = request.form

  newuser = User(username=data['username'], password=data['password'])  # create user object
  response = None
  try:
    #attempt to add user
    db.session.add(newuser)
    db.session.commit()  # save user
    token = create_access_token(identity=newuser.username)
    response = redirect(url_for('index_views.home_page'))
    set_access_cookies(response, token)
    flash('Account Created!')  # send message
  except Exception:  # attempted to insert a duplicate user
    db.session.rollback()
    flash("Username already exists")  # error message
    response = redirect(url_for('auth_views.signup_page'))
  return response

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(request.referrer) 
    flash("Logged Out!")
    unset_jwt_cookies(response)
    return response

'''
API Routes
'''

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
  data = request.json
  token = login(data['username'], data['password'])
  if not token:
    return jsonify(message='bad username or password given'), 401
  response = jsonify(access_token=token) 
  set_access_cookies(response, token)
  return response

# @auth_views.route('/api/identify', methods=['GET'])
# @jwt_required()
# def identify_user():
#     return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response