import csv
from models.loan_application import LoanApplication
from models import db

def handle_loan_application(selection):
    if len(selection) == 1:
        return "CON Enter Farming Experience (in years):"
    elif len(selection) == 2:
        return "CON Enter Land Size (in hectares):"
    elif len(selection) == 3:
        return "CON Enter Annual Income (in Naira):"
    elif len(selection) == 4:
        return "CON Enter Loan Amount (in Naira):"
    elif len(selection) == 5:
        loan_app = LoanApplication(
            farming_experience=int(selection[1]),
            land_size=float(selection[2]),
            annual_income=float(selection[3]),
            loan_amount=float(selection[4])
        )
        db.session.add(loan_app)
        db.session.commit()
        
        # Save to CSV as well
        with open('loan_applications.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([loan_app.id, loan_app.farming_experience, loan_app.land_size, loan_app.annual_income, loan_app.loan_amount])
        
        return "END Loan Application submitted successfully."