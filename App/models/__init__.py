from .user import *
from .internship import internship
import csv
from App.database import db

with open('internship.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        internship = Internship(name=row['Internship Name'],
                                category=row['Category'],
                                duration=row['Duration'],
                                location=row['Location'],
                                description=row['Description'])
        db.session.add(internship)
    db.session.commit()

print('database initialized!')