from .user import *
from .internship import Internship
import csv
from App.database import db

with open('internship.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        internship = Internship(internship_title=row['Internship Name'],
                                company_name=row['Company Name'],
                                location=row['Location'],
                                duration=row['Duration'],
                                stipend=row['Stipend'],
                                start_date=row['Description'])
        db.session.add(internship)
    db.session.commit()

print('database initialized!')