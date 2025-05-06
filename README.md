# 📧 Mailer Class Documentation

The `Mailer` class provides a simple interface for sending plain text and HTML emails via SMTP, with SSL support and dynamic configuration.  
Easily integrate email notifications into your Python projects! 🚀

---

## 🛠️ Requirements

- Python 3.x
- A `config.py` file with:
  - `EMAIL`: your email address (string)
  - `PASSWORD`: your email password or app password (string)
  - `PORT`: SMTP port (integer, e.g., 465 for SSL)

---

## ✨ Usage Example

```python
from mailer import Mailer

mailer = Mailer()  # Uses config.py defaults

# Send a plain text email
mailer.send_mail(
    subject="Test Subject",
    body="This is a test email.",
    from_addr="your@email.com",
    to_addrs=["recipient@email.com"]
)

# Send an HTML email
mailer.send_html_mail(
    subject="HTML Test",
    html_body="<h1>Hello!</h1><p>This is an <b>HTML</b> email.</p>",
    from_addr="your@email.com",
    to_addrs=["recipient@email.com"]
)

# Test SMTP connection
mailer.test_connection()

# Change credentials or server at runtime
mailer.change_credentials("newuser@email.com", "newpassword")
mailer.change_server("smtp.example.com", 587, use_ssl=False)
```

---

## 📚 Class Reference

### `Mailer(smtp_server=None, smtp_port=None, username=None, password=None, use_ssl=True)`

- Initializes the mailer.
- If parameters are omitted, values from `config.py` are used.
- `use_ssl`: If `True`, uses SSL (recommended).

### `send_mail(subject, body, from_addr, to_addrs)`

- Sends a plain text email.
- `to_addrs`: string or list of recipient addresses.
- Returns `True` on success, `False` otherwise.

### `send_html_mail(subject, html_body, from_addr, to_addrs)`

- Sends an HTML email.
- Parameters as above.
- Returns `True` on success, `False` otherwise.

### `test_connection()`

- Tests SMTP login with current credentials.
- Returns `True` on success, `False` otherwise.

### `change_credentials(username, password)`

- Updates the username and password for future emails.

### `change_server(smtp_server, smtp_port, use_ssl=True)`

- Updates the SMTP server, port, and SSL usage.

---

## ⚠️ Error Handling

- All sending methods print errors to the console and return `False` on failure.

---

## 🔗 References

- [Python smtplib documentation](https://docs.python.org/3/library/smtplib.html)
- [Python email.mime documentation](https://docs.python.org/3/library/email.mime.html)
- [Gmail SMTP settings](https://support.google.com/mail/answer/7126229?hl=en)

---

**💡 Note:**  
For Gmail, you may need to use an app password and enable "less secure apps" or use OAuth2.

**Example `config.py`:**
```python
EMAIL = "your@email.com"
PASSWORD = "yourpassword"
PORT = 465  # SSL port