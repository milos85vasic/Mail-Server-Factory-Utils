import ssl
import smtplib

port = 465
smtp_server = "test1.dev.local"
sender_email = "test1@dev.local"
receiver_email = "test2@dev.local"
password = "Test12345"
message = "Test message"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(host=smtp_server, port=port, context=context) as server:
    server.ehlo()
    server.login(sender_email, password)
    server.ehlo()
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
