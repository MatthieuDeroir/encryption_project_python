import smtplib
import ssl



def sendmail():
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    receiver_email = input("Type receiver's email : ")
    sender_email = input("Type sender's email : ")
    password = input("Type sender's email account's password : ")
    msg = "INTRUSION DETECTED !!!\nSomeone failed 5 times to log in !"

    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)

    except Exception as e:
        # Print any error messages to stdout
        print(e)

    finally:
        server.quit()
