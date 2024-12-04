# **Simple Keylogger**

This is a simple Python keylogger designed for ethical and educational purposes only. It logs keystrokes, captures screenshots, records clipboard data, and sends the logs via email. 

> **⚠️ Disclaimer:** This project is intended for educational use only. Unauthorized use of this keylogger is illegal and unethical. Always obtain proper authorization before deploying.

## **Features**
- Logs all keystrokes, including special keys.
- Captures screenshots at regular intervals.
- Logs clipboard content.
- Sends logged data via email.
- Runs in the background using multithreading.

---

## **Configuration**

1. Open the `main.py` file and configure the email settings for sending the logs.

```python
# Email configuration
EMAIL_ADDRESS = "your_email@example.com"  # Your email address
EMAIL_PASSWORD = "your_password"          # Your email password (use app-specific passwords if needed)
SEND_TO_EMAIL = "recipient_email@example.com"  # Email to receive the logs
```

---

## 🚀 **Usage**

### 1. Create and Activate Virtual Environment (Optional, but Recommended)
- For **Windows** Users:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

- For **Linux** Users:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 2. Install the Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the `main.py` File
```bash
python3 main.py
```

The script will continuously log information and send it to the configured email address.

---

## **How It Works**

1. **Key Logging:**
   - Captures all keystrokes and logs them to a file in the current directory.

2. **Screenshot Capture:**
   - Takes a screenshot every 60 seconds and saves it as `screenshot_<timestamp>.png`.

3. **Clipboard Logging:**
   - Monitors and logs changes in clipboard content every 5 seconds.

4. **Email Sending:**
   - Sends the keylog file to the configured email address every hour.

---

## **Files Generated**

- `keylog_<timestamp>.txt`: A file containing all logged keystrokes and clipboard data.
- `screenshot_<timestamp>.png`: Screenshots taken at regular intervals.

---

## **Security Tips**
- Use environment variables to store sensitive information like email addresses and passwords. 
  Example using environment variables:

  ```python
  import os

  EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
  EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
  ```

- Store your credentials securely using `.env` files and libraries like `python-dotenv`.

---

## **Legal and Ethical Considerations**
- **Do not use this keylogger for illegal purposes.**
- Use it only for authorized testing and educational purposes.
- Ensure that you have explicit permission before monitoring any system.

---

## **Contributing**

We welcome contributions! If you'd like to contribute to this Python script, please check out our [Contribution Guidelines](Contribution.md).

---

## **Code of Conduct**
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this project.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Author**
**Santosh Bhandari**  
> Web Developer & Android App Developer  
> [GitHub](https://github.com/santoshvandari)  

---