import praw
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

        """
        email_header = "Content Prospector found a submission of interest on r/" + submission.subreddit
        submission_title = "Title: " + submission.title
        submission_url = submission.url
        """

        email_header = "Email Header"
        submission_title = "Submission title"
        submission_url = "https://www.google.com"

        html = """\
        <html>
            <body>
                <h3>{0}</h3>
                <h4>{1}</h4>
                The submission can be found 
                <a href="{2}">here</a> 
            </body>
        </html>
        """

        # Assemble and return the email
        formatted_html = html.format(email_header, submission_title, submission_url)
        part = MIMEText(formatted_html, "html")
        message.attach(part)
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