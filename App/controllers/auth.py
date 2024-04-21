from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity, verify_jwt_in_request

from App.models import User

def login(username, password):
  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
    return create_access_token(identity=username)
  return None
  
  def get_user_data(user_id):
    user = User.query.get(user_id)  # Assuming query by ID
    if user:
        return {'Current User': user.username}  # Example data
    return None


def setup_jwt(app):
  jwt = JWTManager(app)

  # configure's flask jwt to resolve get_current_identity() to the corresponding user's ID
  @jwt.user_identity_loader
  def user_identity_lookup(identity):
    user = User.query.filter_by(username=identity).one_or_none()
    if user:
        return user.id
    return None


  @jwt.user_lookup_loader
  def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.get(identity)

  return jwt



# Context processor to make 'is_authenticated' available to all templates
def add_auth_context(app):
  @app.context_processor
  def inject_user():
      try:
          verify_jwt_in_request()
          user_id = get_jwt_identity()
          current_user = User.query.get(user_id)
          is_authenticated = True

          is_admin = True if user_id == 1 else False   #added - only admin is with id 1!
      except Exception as e:
          print(e)
          is_authenticated = False
          current_user = None

          is_admin = False   #added - if not authenticated, then not user, and as such not admin
      return dict(is_authenticated=is_authenticated, current_user=current_user, is_admin=is_admin)

