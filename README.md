# Gmail Python Function
Python function for sending emails using gmail (or other providers)

## Requirements

Gmail Account

Python

Pip

## Setup

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate the virtual environment

```bash
./venv/scripts/activate
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Replace EMAIL_FROM and app_password with your gmail (or other provider's) details.
You can follow these instructions for Gmail

[Gmail Link](https://support.google.com/domains/answer/9437157?hl=en)

```python
    EMAIL_FROM = "youremail@gmail.com"
    app_password = "000000000000" # you can create an app password from your gmail account security settings
```

5. Replace "example@gmail.com" with the email to send. Then run the function

```python
response = send_email("example@gmail.com", [], "Testing Function", "Hi there. It's working well")
```

6. Run the function

```bash
python app.py
```
