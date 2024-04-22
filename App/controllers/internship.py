from App.models import Internship
from App.database import db
import csv 
# import os


# DATABASE_URL = os.environ['postgres://internships_user:JC9Rqcm1wRoDfOzOTvAirGf69j07tLUS@dpg-coir5t0l5elc73dccv60-a/internships']
# conn = psycopg2.connect(DATABASE_UR)


# def initialize_internship():  
#   with open('App/static/internship.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader) 
#     for row in csv_reader:
#       new_internship = Internship(row[0], row[1], row[2], row[3], row[4], row[5])
#       db.session.add(new_internship)

#   try:
#     db.session.commit()
#   except Exception as e:
#     print("An error occurred during commit:", e)

import psycopg2


def initialize_internship():
  try:
    # Connect to the database using environment variables
    DATABASE_URL = os.environ['postgres://internships_user:JC9Rqcm1wRoDfOzOTvAirGf69j07tLUS@dpg-coir5t0l5elc73dccv60-a/internships']
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Open the CSV file
    with open('internship.csv', 'r') as file:
      csv_reader = csv.reader(file)
      next(csv_reader)  # Skip the header row

      # Read data into a list of lists
      data = list(csv_reader)

    # Prepare SQL statement (assuming column names match your CSV)
    sql = """
        INSERT INTO internships (title, company_name, location, start_date, duration, stipend)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Insert data using a loop
    for row in data:
      # Extract and format data (adjust based on your CSV format)
      title, company, location, start_date, duration, stipend = row
      # Assuming stipend is a string like "$30,000/month", extract the numerical value
      stipend_amount = int(stipend.split()[1].replace(",", ""))

      # Execute the insert statement with the extracted data
      cur.execute(sql, (title, company, location, start_date, duration, stipend_amount))

    conn.commit()
    print("Internships successfully added!")
  except Exception as e:
    print("An error occurred:", e)
    conn.rollback()  # Rollback changes in case of errors

if __name__ == "__main__":
  initialize_internship()


if __name__ == "__main__":
  initialize_database()


def create_project(internship_title,company_name,location,start_date,duration,stiped):
  newproject=Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,duration=duration,stipend=stiped)
  db.session.add(newproject)
  db.session.commit()
  return newproject


