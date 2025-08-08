Automated Email Scheduler in Python

This is a simple Python project that allows you to automatically send emails based on a schedule, using data from a CSV file. It is ideal for learning and showcasing my skills in automation, data handling, and scripting.

Purpose:

The project was built as part of a programming portfolio, demonstrating the use of:
Task scheduling using the schedule library
Email automation with yagmail
CSV file handling
Continuous execution of scheduled tasks

Features:

Read email schedules from a CSV file
Automatically send emails at the scheduled time
Support for multiple recipients and custom messages
Clean, beginner-friendly Python code

Project struture:

email_scheduler/

├── script.py       # Main script

└── email.csv         # CSV file with scheduled emails

CSV Format (emails.csv)
email,subject,message,time
```Python
example1@email.com,Subject 1,Message for example 1,08:00
example2@email.com,Subject 2,Message for example 2,09:30
```
How to Use
Clone this repository:
```Bash
git clone https://github.com/MatheusJuski/Email-Scheduler.git
cd Email-Scheduler
```
Install dependencies:
```python
pip install schedule yagmail
```

Configure your sender email:
Edit agendador.py and set your email and app password:

```Python
EMAIL = "youremail@gmail.com"
PASSWORD = "your_app_password"
```
⚠️ For Gmail users, make sure to enable 2FA and generate an App Password.
Edit the emails.csv file with the emails you want to send.

Run the scheduler with:
```Python
python agendador.py
```


Possible Improvements
Support for file attachments
Web interface (using Flask or Django)
HTML email body support
Store schedule in a database
Logging of sent emails

License
This project is licensed under the MIT License.

Author
Created by Matheus Juski

