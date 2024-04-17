from .user import *
from .internship import Internship
import csv
from App.database import db

def initialize_database():  
  with open('internship.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) 
    for row in csv_reader:
      new_internship = Internship(row[0], row[1], row[2], row[3], row[4], row[5])
      db.session.add(new_internship)

  try:
    db.session.commit()
  except Exception as e:
    print("An error occurred during commit:", e)

if __name__ == "__main__":
  initialize_database()
