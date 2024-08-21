Here’s a comprehensive GitHub repository description for the simple keylogger program:

---

# Simple Python Keylogger

This repository contains a simple Python keylogger created for educational purposes, demonstrating how keystrokes can be captured and logged into a file. The keylogger makes use of the `pynput` library to listen to keyboard events and record them. **This tool should only be used with explicit consent and for legal purposes.**

## Features

- **Keystroke Logging**: Captures and logs every key pressed, including letters, numbers, and special characters such as `space`, `tab`, and `enter`.
- **Log File Output**: All captured keystrokes are saved to a file called `key_log.txt` for review.
- **Exit on Escape Key**: The program stops logging and exits when the escape key (`esc`) is pressed.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Hun33er/PRODIGY_WD_04/simple-keylogger.git
   ```

2. **Install dependencies**:
   Ensure you have Python installed. Then, install the required library using pip:
   ```bash
   pip install pynput
   ```

3. **Run the program**:
   After installation, you can start the keylogger by running:
   ```bash
   python keylogger.py
   ```

## Example Output

The keylogger records all keystrokes in a file named `key_log.txt`. For example:

```
Hello World
[TAB]This is a keylogger[ENTER]
```

## Important Notes

- **Ethical Use Only**: This keylogger is intended strictly for educational purposes and personal use on systems where you have permission. Unauthorized use to capture data without consent is **illegal** and **unethical**.
- **Logging Special Keys**: Special keys such as `enter`, `tab`, and `space` are logged in a human-readable format like `[ENTER]`, `[TAB]`, etc.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This description provides clarity on the purpose of the keylogger, its installation process, and most importantly, emphasizes ethical usage.
