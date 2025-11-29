Pornhub Account Flow Automation (QA Portfolio Project)

This project is part of my QA Automation Engineer portfolio.
It demonstrates a full end-to-end automated workflow on Pornhub.com, showcasing skills in Playwright automation, email verification testing, UI handling, resilient selectors, and high-volume scenario testing.

🚀 Overview

This automation script:

Visits https://www.pornhub.com/

Automates the sign-up flow

Retrieves a verification code from my mailbox

Enters the 6-digit code into Pornhub’s verification modal

Completes DOB and TOS dialogs

Takes screenshots

Performs automated sign-in testing

Repeats the entire workflow for stress testing & captcha behavior observation

This project is designed to showcase my QA abilities, not to create real accounts or bypass security.

🔧 Features

Automated navigation and modal handling

Form completion and validation checking

Email verification code retrieval

Selector strategy for a dynamic UI

Error-handling and fallback logic

Loop-based repeated testing (up to 1000 runs)

Screenshot generation for each iteration

Demonstrates detection of captcha triggers

📂 Project Structure
/project
 ├─ browser_manager.py
 ├─ utils.py
 ├─ main.py
 ├─ screenshots/
 └─ README.md

🧪 QA Skills Demonstrated

End-to-end UI automation

Email verification workflow testing

Modal/overlay handling

Working with unstable selectors

High-volume testing & behavior monitoring

Asynchronous Python automation

Playwright experience (page flows, locators, modal detection)

Debugging with screenshots

Error recovery & retry logic

📝 How the Script Works
🔹 Sign-Up Flow

Open Pornhub

Dismiss age verification

Accept cookie banner

Open Sign Up

Enter email + password

Fetch verification code

Input 6 digits individually

Handle DOB modal

Handle TOS modal

Confirm sign-up via profile menu

🔹 Sign-In Flow

Open Pornhub

Dismiss modals

Enter credentials

Complete any re-shown prompts

Confirm login by opening profile menu

🔹 Runner

Performs the sign-up flow repeatedly to test:

UI stability

Modal frequency changes

CAPTCHA escalation

Error occurrences

⚙️ Requirements
Python 3.9+
Playwright
Mailbox access for reading verification codes


Install dependencies:

pip install playwright
playwright install

▶️ Run the Script
python main.py


Screenshots will be saved to:

screenshots/<username>_screenshot.png

⚠️ Ethical & Portfolio Notice

This project was created exclusively for QA portfolio purposes.
The automated accounts were test accounts, and the script is not intended for real-world account creation, bypassing captcha, or violating Pornhub.com’s Terms of Service.

The goal is to demonstrate automation engineering skills only.

📬 Future Enhancements

Structured logging

Retry strategies per modal

Visual reports (HTML or Allure)

Proxy routing for research

Parallel runner