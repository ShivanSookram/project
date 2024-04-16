from App.database import db

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    internship_title = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    start_date = db.Column(db.Date, nullable=False)  
    duration = db.Column(db.String, nullable=False)  
    stipend = db.Column(db.Float, nullable=False)

    def __init__(self, internship_title, company_name, location, start_date, duration, stipend):
        self.internship_title = internship_title
        self.company_name = company_name
        self.location = location
        self.start_date = start_date
        self.duration = duration
        self.stipend = stipend

    def __repr__(self):
        return f"<Internship {self.internship_title} {self.company_name}>"
