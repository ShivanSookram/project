from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String(120), nullable=False)
  type = db.Column(db.String(50))
  __mapper_args__ = {'polymorphic_identity': 'user', 'polymorphic_on': type}

  def __init__(self, username, password):
    self.username = username
    self.set_password(password)

  def get_json(self):
    return {
      'id': self.id,
      'username': self.username
    }

  def set_password(self, password):
    """Create hashed password."""
    self.password = generate_password_hash(password)

  def check_password(self, password):
    """Check hashed password."""
    return check_password_hash(self.password, password)


class Admin(User):
  __tablename__ = 'admin'
  staff_id = db.Column(db.String(120), unique=True)
  __mapper_args__ = {'polymorphic_identity': 'Admin', }

  def __init__(self, staff_id, username, password):
    super().__init__(username, password)
    self.staff_id = staff_id

  def get_json(self):
    return {
      "id": self.id,
      "username": self.username,
      "staff_id": self.staff_id,
      "type": self.type
    }

  def __repr__(self):
    return f'<Admin {self.id} : {self.username}>'


class RegularUser(User):
  __tablename__ = 'regular_user'
  __mapper_args__ = {
    'polymorphic_identity': 'regular user',
  }
