import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config  # Import your config.py

class Mailer:
    def __init__(self, smtp_server=None, smtp_port=None, username=None, password=None, use_ssl=True):
        self.smtp_server = smtp_server if smtp_server else "smtp.gmail.com"  # Default SMTP server
        self.smtp_port = smtp_port if smtp_port else config.PORT
        self.username = username if username else config.EMAIL
        self.password = password if password else config.PASSWORD
        self.use_ssl = use_ssl

    def send_mail(self, subject, body, from_addr, to_addrs):
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = ', '.join(to_addrs) if isinstance(to_addrs, list) else to_addrs
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            if self.use_ssl:
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
                    server.sendmail(from_addr, to_addrs, msg.as_string())
            else:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
                    server.sendmail(from_addr, to_addrs, msg.as_string())
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def send_html_mail(self, subject, html_body, from_addr, to_addrs):
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = ', '.join(to_addrs) if isinstance(to_addrs, list) else to_addrs
        msg['Subject'] = subject
        msg.attach(MIMEText(html_body, 'html'))

        try:
            if self.use_ssl:
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
                    server.sendmail(from_addr, to_addrs, msg.as_string())
            else:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
                    server.sendmail(from_addr, to_addrs, msg.as_string())
            return True
        except Exception as e:
            print(f"Failed to send HTML email: {e}")
            return False

    def test_connection(self):
        try:
            if self.use_ssl:
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
            else:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
            print("SMTP connection successful.")
            return True
        except Exception as e:
            print(f"SMTP connection failed: {e}")
            return False

    def change_credentials(self, username, password):
        self.username = username
        self.password = password

    def change_server(self, smtp_server, smtp_port, use_ssl=True):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.use_ssl = use_ssl
