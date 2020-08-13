import praw
import parser
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ContentNotifier:
    def __init__(self):
        config_parser = parser.ConfigParser()
        email_credentials = config_parser.parse_email_credentials()
        self.sender_email = email_credentials['sender_email']
        self.sender_password = email_credentials['sender_password']
        self.receiver_email = email_credentials['receiver_email']

    def create_email(self, sender_email, receiver_email, submission):
        # Define contents of email notification
        message = MIMEMultipart("alternative")
        message["Subject"] = "Content Prospector found a gem"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        email_header = "Content Prospector found a submission of interest on r/" + submission.subreddit.display_name
        submission_title = submission.title
        submission_url = submission.url
    
        html = """\
        <html>
            <body>
                <h3>{0}</h3>
                <h4>{1}</h4>
                <h5>
                    The submission can be found 
                    <a href="{2}">here</a> 
                </h5>
            </body>
        </html>
        """

        # Assemble and return the email
        formatted_html = html.format(email_header, submission_title, submission_url)
        part = MIMEText(formatted_html, "html")
        message.attach(part)
        return message.as_string()

    def send_email_notification(self, submission):
        # Data needed to establish SSL connection and send email
        port = 465

        # Create email with content
        email_notification = self.create_email(self.sender_email, self.receiver_email, submission)

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, email_notification)

if __name__ == "__main__":
    c = ContentNotifier()
    c.send_email_notification(None)