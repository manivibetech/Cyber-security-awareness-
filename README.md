# phishing email detacor 

🔐 Phishing Email Detector

A Python-Based School Project for Detecting Suspicious Emails

📌 Project Description

The Phishing Email Detector is a simple Python program designed to identify potentially suspicious or phishing emails.

It analyzes email text and sender addresses to detect warning signs such as urgent messages, suspicious links, requests for sensitive information, and suspicious sender addresses.

This project is developed for educational purposes to demonstrate basic cybersecurity concepts using Python.

✨ Features

- 🚨 Detects urgent or threatening phrases.
- 🔗 Identifies potentially suspicious links.
- 📧 Checks sender email addresses for certain suspicious patterns.
- 🔑 Detects requests for sensitive information, such as passwords and OTPs.
- 📊 Calculates a suspiciousness score.
- 🛡️ Classifies emails as potentially phishing or not flagged as phishing.
- 📝 Displays reasons why an email was flagged.

🛠️ Technologies Used

- Programming Language: Python 3
- Module: "re" (Regular Expressions)
- Additional Libraries: None

📂 Project Structure

phishing-detector/
│
├── phishing_detector.py
└── README.md

⚙️ Requirements

- Python 3 installed on your computer or Android device.
- A text editor or Python-compatible IDE.

No additional Python packages are required.

🚀 How to Run

Step 1: Download or Save the Project

Save the Python code in a file named:

"phishing_detector.py"

Step 2: Open a Terminal

Navigate to the folder containing your project.

Step 3: Run the Program

Execute the following command:

python phishing_detector.py

If your system uses "python3", run:

python3 phishing_detector.py

Step 4: View the Results

The program will analyze two sample emails and display their suspiciousness scores, classifications, and detection reasons.

🧪 Example

Sample Email 1

Dear user, your account has been suspended.
Please click here http://bit.ly/secure-login urgently
to verify your password immediately.

Expected result: The email should be flagged as potentially phishing because it contains suspicious indicators.

Sample Email 2

Hi Ali, meeting tomorrow at 10am in class.
Please bring your science notes.

Expected result: The email should not be flagged by the current detection rules.

Note: Exact scores and results depend on the detection rules implemented in the Python code.

🔍 How It Works

The program uses a simple rule-based scoring system.

Detection Rule| Score
Contains an urgent phrase| +1
Contains a potentially suspicious link| +2
Contains a suspicious sender pattern| +1
Requests sensitive information| +2
Classification threshold| 3 points

The program checks the email text and adds points when it finds matching indicators.

If the total score is 3 or higher, the email is flagged as potentially phishing.

Otherwise, it is not flagged by the current rules.

⚠️ Limitations

- The program uses basic keyword matching rather than advanced machine learning.
- Not every URL is malicious, and not every suspicious-looking URL is dangerous.
- Trusted sender domains are hardcoded for demonstration purposes and should not automatically be considered safe.
- The current sender-checking logic only flags certain addresses containing words such as "support" or "security" when they do not match the listed trusted domains.
- Legitimate emails may be flagged incorrectly.
- Phishing emails may pass undetected.
- The program does not connect to an email account or automatically scan an inbox.

Important: This tool is intended for educational demonstrations. It should not be used as the sole method for deciding whether an email is safe.

🔒 Cybersecurity Safety Tips

- Never share your password or OTP through suspicious links.
- Verify the sender before responding to unexpected emails.
- Avoid opening unknown attachments.
- Visit official websites directly instead of following unexpected login links.
- Enable two-factor authentication whenever possible.

🎓 Educational Purpose

This project demonstrates introductory Python programming, regular expressions, keyword detection, conditional logic, and basic cybersecurity awareness.

It can be extended with URL reputation checks, a graphical user interface, improved sender validation, or machine-learning-based classification.

👨‍💻 Author

School Project — Phishing Email Detector

📜 License

This project is provided for educational and learning purposes.📱 Ab 
