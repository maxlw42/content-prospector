import smtplib
import ssl
import email

class ContentNotifier:
    def __init__(self):
        self.password = None

    def create_email(self, submission):
        return None

    def send_email_notification(self, submission):
        port = 465  # For SSL
        password = input("Type your password and press enter: ")
        sender = input("Type the sender of the email: ")
        receiver = input("Type the intended receiver of the email: ")
        message = """\
            Hi there

            This message is sent from Python."""

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)

if __name__ == "__main__":
    c = ContentNotifier()
    c.send_email_notification(None)