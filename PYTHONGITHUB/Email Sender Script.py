import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'
subject = 'hello hello'
body = 'hello from david moogy '

# Function to send email
def send_email(subject, body, to_email):
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection

        # Log in to the server
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        # Disconnect from the server
        server.quit()

if __name__ == "__main__":
    print("Sending email...")
    send_email(subject, body, recipient_email)
    print("Email sending process complete.")
