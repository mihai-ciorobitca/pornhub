# 📌 Pornhub Account Automation – QA Portfolio Project

This project is part of my **QA Automation Engineering portfolio**.  
It showcases my ability to build **complex, end-to-end automated flows** using **Playwright**, including:

- UI automation  
- Email verification  
- Modal handling  
- Stress testing  
- Captcha observation  
- Repeated workflow execution  

The automation interacts with **https://www.pornhub.com** because its multi-step registration flow provides a realistic example of a dynamic, real-world UI.

⚠️ **Disclaimer:**  
This project is for **portfolio and educational purposes only**.  
It is **not** intended to bypass security, create real accounts, or violate Terms of Service.

---

## 🧭 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [QA Skills Demonstrated](#qa-skills-demonstrated)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Example Code Snippet](#example-code-snippet)
- [Installation](#installation)
- [Running the Script](#running-the-script)
- [Ethical Notice](#ethical-notice)
- [Future Enhancements](#future-enhancements)

---

## 📌 Overview

This script automates the entire **signup + verification + login** workflow on Pornhub.com.  
Key capabilities:

- Fills forms  
- Handles modals  
- Retrieves real email verification codes  
- Inputs 6-digit codes into UI fields  
- Completes DOB and TOS prompts  
- Takes final screenshots  
- Repeats workflow for stress testing (up to 1000 iterations)

---

## ✨ Features

- **Automated sign-up workflow**
- **Email verification handling**
- **DOB + TOS modal automation**
- **Sign-in workflow**
- **Screenshot capture**
- **Stress-testing loop**
- **Captcha trigger observation**
- **Async Playwright browser management**

---

## 🧪 QA Skills Demonstrated

- End-to-end UI automation  
- Testing verification-based flows  
- Dynamic locator handling  
- Working with modal logic  
- Error recovery + exception handling  
- High-volume workflow execution  
- Asynchronous programming  
- Real-world debugging using screenshots  
- Selector strategy for unstable UIs  
- Handling repeated executions until captcha triggers

---

## 📂 Project Structure

/project
├─ browser_manager.py
├─ utils.py
├─ main.py
├─ screenshots/
└─ README.md


---

## 📝 How It Works

### **1. Sign-Up Flow**
- Navigate to Pornhub  
- Handle age and cookie banners  
- Open sign-up dialog  
- Fill email and password  
- Wait for email verification modal  
- Retrieve verification code via `get_verification_code()`  
- Input digits into UI fields  
- Handle "Date of Birth" modal if shown  
- Accept "Terms of Service" modal  
- Confirm success through profile menu  

### **2. Sign-In Flow**
- Navigate to homepage  
- Handle modals  
- Enter credentials  
- Complete DOB/TOS if shown  
- Confirm login  

### **3. Runner Loop**
Loops the automation up to **1000 times**: