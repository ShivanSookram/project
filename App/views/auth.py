from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies, get_jwt_identity

from.index import index_views
from App.controllers import auth


from App.models import db, Internship, User

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

    # Render template or return JSON based on authorization
    if current_user_id == 2:  # Assuming admin ID is 2 (change if needed)
        return render_template('admin.html', user_data=user_data)
    else:
        return jsonify({'message': 'Unauthorized access'}), 403
        


    

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password'])
    response = redirect(request.referrer)
    if not token:
        flash('Bad username or password given'), 401
    else:
        flash('Login Successful')
        set_access_cookies(response, token) 
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