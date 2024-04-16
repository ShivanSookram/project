from .user import *
from .internship import internship

# Read data from the "internship.csv" file
with open('internship.csv', 'r') as file:
    data = file.readlines()

# Store data in the "internship" table
for line in data:
    # Assuming each line in the CSV file represents a record with comma-separated values
    values = line.strip().split(',')
    internship = internship(*values)
    internship.save()
