from .user import *
from .internship import Internship
import csv
from App.database import db

with open('internship.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    internship = Internship(internship_title=row['internship_title'],
                             company_name=row['company_name'],
                             location=row['location'],
                             start_date=row['start_date'],
                             duration=row['duration'],
                             stipend=row['stipend'])
    
    db.session.add(internship)
db.session.commit()

print('database initialized!')
