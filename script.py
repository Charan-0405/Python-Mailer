import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
def send_mail(workflow_name,repo_name,workflow_run_id):
    sender_email=os.getenv('SENDER_EMAIL')
    sender_password=os.getenv('SENDER_PASSWORD')
    reciver_email=os.getenv('RECIVER_EMAIL')
    subject = f"Workflow {workflow_name} failed for repo {repo_name}"
    body = f"Hi, the workflow {workflow_name} failed for the repo {repo_name}. Please check the logs for more details.\nMore Details: \nRun_ID: {workflow_run_id}"
    msg=MIMEMultipart()
    msg['From']=sender_email
    msg['To']=reciver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)
        text=msg.as_string()
        server.sendmail(sender_email,reciver_email,text)
        server.quit()
        print('Email sent succesfully')
    except Excetion as e:
        print(f'Error:{e}')
send_mail(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))
