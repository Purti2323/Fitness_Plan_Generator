FitPlan-AI: Personalized Fitness Plan Generator
A web-based fitness application designed to provide personalized workout plans with a secure authentication system.

Milestone 3: Login System with OTP Verification
This milestone implements a secure authentication flow using JWT and email-based OTP verification.

Features
User Registration: Sign up using Email ID and Password.
Secure Authentication: Login verification against a database.
OTP Security: Automated 6-digit OTP generation and delivery via SendGrid upon successful credentials check.
Access Control: Dashboard access is restricted to verified users only.

Folder Structure
Plaintext
FitPlan-AI/
├── Milestone3/
├── app.py           # Main application logic and UI
├── database.py      # Database initialization and user functions
├── auth.py          # JWT and OTP authentication logic
├── email_utils.py   # SendGrid integration for OTP delivery
├── requirements.txt # Project dependencies
├── README.md        # Documentation
└── screenshots/     # Application demo images

Getting Started
Prerequisites
Python 3.x
A SendGrid account (for email functionality)

Installation
Clone the repository:
git clone https://github.com/Purti2323/FitPlan-AI-Personalized-Fitness-Plan-Generator.git

Install the required dependencies:
pip install -r requirements.txt

Set up your environment variables (e.g., database URI, SendGrid API Key).

Run the application:
python app.py


Built With
streamlit
python
SQLite
SendGrid API
