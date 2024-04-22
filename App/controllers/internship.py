from App.models import Internship
from App.database import db
import csv 

def initialize_internship():
    try:
        with open('/static/internship.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row (optional)

            internships = []
            for row in csv_reader:
                new_internship = Internship(row[0], row[1], row[2], row[3], row[4], row[5])
                internships.append(new_internship)

            # Save the processed internships (assuming a method exists)
            save_internships(internships)  # You might need to add this function
            
            # No longer tries to use `generate_html` directly

    except FileNotFoundError:
        print("Error: Internship CSV file not found!")

# Function to save internships to database (example)
def save_internships(internships):
    for internship in internships:
        db.session.add(internship)
    db.session.commit()



if __name__ == "__main__":
  initialize_database()


def create_project(internship_title,company_name,location,start_date,duration,stiped):
  newproject=Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,duration=duration,stipend=stiped)
  db.session.add(newproject)
  db.session.commit()
  return newproject


