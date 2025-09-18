import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import logging
import os

# ----------------------
# Configurations
# ----------------------
LOG_FILE = "logs.txt"
ERROR_THRESHOLD = 0.3  # 30% of logs are errors
CHECK_INTERVAL = 10    # seconds

# Gmail credentials
GMAIL_USER = "shashankkanade01@gmail.com"       # Set in environment
GMAIL_PASSWORD = "tbfk faba klpo asya"
TO_EMAIL = "shashank.kanade@sdbi.in"           # Recipient

# ----------------------
# Logging configuration
# ----------------------
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------
# Function to send email alert
# ----------------------
def send_email_alert(error_rate):
    subject = "ALERT! Error rate exceeded threshold"
    body = f"Current error rate is {error_rate:.2f}, which exceeds threshold {ERROR_THRESHOLD:.2f}"

    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Alert sent via email: {body}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# ----------------------
# Function to inject mock data
# ----------------------
def generate_mock_log():
    # 70% chance success, 30% chance error
    if random.random() < 0.7:
        logging.info(f"Prediction successful: input={random.randint(1,100)}, output={random.uniform(1,100):.2f}")
    else:
        logging.error(f"Prediction failed: input={random.randint(-50,0)}, error=Mock bad data")

# ----------------------
# Monitoring loop
# ----------------------
print("Monitor started...")

while True:
    # Generate mock logs for demonstration
    generate_mock_log()

    # Read logs
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        time.sleep(CHECK_INTERVAL)
        continue

    total_logs = len(lines)
    error_logs = sum(1 for line in lines if "ERROR" in line)
    error_rate = error_logs / total_logs

    print(f"Total logs: {total_logs}, Errors: {error_logs}, Error rate: {error_rate:.2f}")

    if error_rate > ERROR_THRESHOLD:
        send_email_alert(error_rate)

    time.sleep(CHECK_INTERVAL)
