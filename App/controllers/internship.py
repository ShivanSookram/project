from App.models import Internship
from App.database import db
import csv 
from App.views import index_page


def initialize_internship():
    try:
        with open('/static/internship.csv', 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row (optional)

            internships = []
            for row in csv_reader:
                new_internship = Internship(row[0], row[1], row[2], row[3], row[4], row[5])
                internships.append(new_internship)

            # Assuming `index_page` is already defined and contains the HTML content
            html_content = index_page
            return html_content

    except FileNotFoundError:
        print("Error: Internship CSV file not found!")


if __name__ == "__main__":
  initialize_database()


def create_project(internship_title,company_name,location,start_date,duration,stiped):
  newproject=Internship(internship_title=internship_title,company_name=company_name,location=location,start_date=start_date,duration=duration,stipend=stiped)
  db.session.add(newproject)
  db.session.commit()
  return newproject


