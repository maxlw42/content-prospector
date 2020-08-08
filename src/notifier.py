import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ContentNotifier:
    def __init__(self):
        self.password = None

    def create_email(self, sender_email, receiver_email, submission):
        # Define contents of email notification
        message = MIMEMultipart("alternative")
        message["Subject"] = "Content Prospector found a gem"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = "Content Prospector found a submission of interest on r/FrugalMaleFashion"
        html = """\
        <html>
            <body>
                <a href="http://www.realpython.com">Real Python</a> 
                has many great tutorials.
            </body>
        </html>
        """

        # Assemble the email
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        return message.as_string()


    def send_email_notification(self, submission):
        # Data needed to establish connection and send email
        port = 465  # For SSL
        sender_email = input("Type the sender of the email: ")
        sender_password = input("Type the sender's password: ")
        receiver_email = input("Type the receiver's email: ")

        # Create email with content
        email_notification = self.create_email(sender_email, receiver_email, submission)

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, email_notification)

if __name__ == "__main__":
    c = ContentNotifier()
    c.send_email_notification(None)