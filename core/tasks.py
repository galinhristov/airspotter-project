import threading
import time

def send_welcome_email(user_email):
    # simulate delay (like real async work)
    time.sleep(3)

    print(f'Welcome email sent to {user_email}')


def send_welcome_email_async(user_email):
    thread = threading.Thread(
        target=send_welcome_email,
        args=(user_email,)
    )
    thread.start()
