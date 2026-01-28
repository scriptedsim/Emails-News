import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "simeenayman2@gmail.com"
    password = "qjzntedgyqrikxjg"

    receiver = "simeenayman233@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

# Only runs if you play THIS file directly, not when imported
if __name__ == "__main__":
    send_email("Hello")