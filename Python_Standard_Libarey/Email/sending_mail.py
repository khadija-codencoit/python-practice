from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib
import csv


# message = MIMEMultipart()
# message["from"] = "Fahmid"
# message["to"] = "khatukhadija556@gmail.com"
# message["subject"] = "This is subject"
# message.attach(MIMEText("Body text More"))
# message.attach(MIMEImage(Path("Python_Standard_Libarey/images.jpg").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()                # Step 1: Say hello to the server
#     smtp.starttls()            # Step 2: Start encrypted communication (TLS)
#     smtp.login("juhairfahmid.codencoit@gmail.com", "fgbr wrvf fjrx cgea")   # Step 3: Log in with your email and password
#     smtp.send_message(message)  # Step 4: Send the email message you created
#     print("Sent....go")


##Practice

template = Template(Path("Python_Standard_Libarey/template.html").read_text())

with open("company_emails.csv","w",newline="") as output:
    write = csv.writer(output)
    write.writerow(["Employe Names" , "Emails"])
    write.writerow(["Khadija" , "khatukhadija556@gmail.com"])
    write.writerow(["Khadija Khatun" , "khadija.khatun@codencoit.com"])
    write.writerow(["Juhair Fahmid" ,"juhair.fahmid@codencoit.com "])
    write.writerow(["Anik Das" ,"anik@codencoit.com "])
    write.writerow(["Jerin" ,"jerin.tasnim@codencoit.com "])
   

with open("company_emails.csv","r",newline = "") as output:
    read_email = csv.DictReader(output)
    for row in read_email:
        email= row.get("Emails")

        message = MIMEMultipart()
        message["from"] = "Khadija Khatun"
        message["to"] = email
        message["subject"] = "Team Meetup Notification."
        body = template.substitute({"name":row.get("Employe Names")})
        message.attach(MIMEText(body,"html"))
        

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

            smtp.ehlo()
            smtp.starttls()
            smtp.login("khadija.codencoit@gmail.com", "erws ccfb gzwh nhip") 
            smtp.send_message(message)
            print(f" Sending Email to {row.get("Emails")} is done. ")



    


