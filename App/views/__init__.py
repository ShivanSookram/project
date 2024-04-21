# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .form import form_views
from .company import company_views

views = [user_views, index_views, auth_views, form_views,company_views] 
# blueprints must be added to this list