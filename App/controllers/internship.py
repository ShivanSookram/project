from App.models import Internship
from App.database import db
import csv 
# import os


# DATABASE_URL = os.environ['postgres://internships_user:JC9Rqcm1wRoDfOzOTvAirGf69j07tLUS@dpg-coir5t0l5elc73dccv60-a/internships']
# conn = psycopg2.connect(DATABASE_UR)


# def initialize_internship():  
#   with open('App/static/internship.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)
#     next(csv_reader) 
#     for row in csv_reader:
#       new_internship = Internship(row[0], row[1], row[2], row[3], row[4], row[5])
#       db.session.add(new_internship)

import csv
import psycopg2


def initialize_internship():
  try:
    # Connect to the database using environment variables
    DATABASE_URL = os.environ['DATABASE_URL']
    # conn is referenced here but not assigned yet

    cur = psycopg2.connect(DATABASE_URL)
    cur.cursor()  # Using cur before conn is defined

    # Assuming your CSV data is accessible within the application (adjust the path)
    with open('internship.csv', 'r') as file:  # Replace with the actual path to your CSV
      csv_reader = csv.DictReader(file)
      next(csv_reader)  # Skip the header row

      # Prepare SQL statement (assuming column names match your CSV)
      sql = """
          INSERT INTO internships (title, company_name, location, start_date, duration, stipend)
          VALUES (%s, %s, %s, %s, %s, %s)
      """

      # Insert data using a loop
      for row in csv_reader:
        cur.execute(sql, tuple(row.values()))  # Use unpacking for values

      conn.commit()  # conn is used here before it's defined
      print("Internships successfully added!")
  except Exception as e:
    print("An error occurred:", e)
  finally:
    conn.close()  # conn is used here before it's defined

if __name__ == "__main__":
  initialize_internship()



  try:
    db.session.commit()
  except Exception as e:
    print("An error occurred during commit:", e)

if __name__ == "__main__":
  initialize_database()


def create_project(internship_title,company_name,location,start_date,duration,stiped):
  newproject=Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,duration=duration,stipend=stiped)
  db.session.add(newproject)
  db.session.commit()
  return newproject


