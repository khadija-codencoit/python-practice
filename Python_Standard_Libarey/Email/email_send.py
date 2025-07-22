import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
# Email credentials

template = Template(Path("Python_Standard_Libarey/Email/Teamplate/routine.html").read_text())

# Read the routine from CSV
with open("csv-files/weekplan_ota_sheet1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        name = row["Team Member"]
        email = row["Emails"]

        html_content = template.substitute({
            "name": name,
            "saturday": row["Saturday"],
            "sunday": row["Sunday"],
            "monday": row["Monday"],
            "tuesday": row["Tuesday"],
            "wednesday": row["Wednesday"],
            "thursday": row["Thursday"],
            "friday": row["Friday"]
        })

    

        # Compose the email
        message = MIMEMultipart()
        message["From"] = "Khadija Khatun"
        message["To"] = email
        message["Subject"] = "Your Weekly Shift Routine"
        message.attach(MIMEText(html_content, "html"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login("khadija.codencoit@gmail.com", "erws ccfb gzwh nhip")
            smtp.send_message(message)
            print(f"Sent routine to {name} at {email}")
