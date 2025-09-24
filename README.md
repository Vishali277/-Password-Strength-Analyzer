🔐 Python Password Strength Analyzer 🔐
A robust command-line tool built to evaluate password strength against modern security criteria. This project serves as a practical exploration of cyber hygiene and secure credential practices.

🚀 Project Overview
The goal of this task was to develop a functional password analyzer to gain a hands-on understanding of what constitutes a strong, secure password. The script provides instant feedback, rating passwords as Weak, Medium, or Strong, and offers specific, actionable advice for improvement. This helps to illustrate why password policies are a fundamental aspect of cybersecurity.

✨ Features
Multi-Criteria Analysis: Checks for length, uppercase letters, lowercase letters, numbers, and special characters.

Intuitive Scoring System: Assigns a score based on complexity to provide a clear strength rating.

Actionable Feedback: Instantly tells the user exactly what is missing from their password.

Interactive CLI: A simple and user-friendly command-line interface for easy testing.

📊 Demonstration Results
The tool was tested with a variety of passwords to demonstrate its analysis capabilities. The results are summarized below:

Password Input

Strength Rating

Feedback Provided

password

Weak

❌ Needs length, uppercase, number, & special character.

Password123

Medium

❌ Missing a special character (e.g., !@#$%).

S@fep4ssw0rd!

Strong

✅ All criteria met.

12345

Weak

❌ Needs length, uppercase, lowercase, & special character.

Screenshots of these live tests are available in the screenshots/ directory.

💡 Key Concepts & Learnings
Password Entropy: This project clearly shows that entropy (a measure of randomness and complexity) is crucial. Adding character variety and length makes a password exponentially more resistant to brute-force and dictionary attacks.

The Human Factor: Simple, predictable passwords are the weakest link in security. This tool helps visualize why user education on creating strong credentials is so important.

Input Validation: The script is a practical example of input validation, a core concept where user-provided data is checked against a set of rules to ensure it meets security and quality standards.


📁 Files in This Repository
password_checker.py: The Python source code for the tool.

README.md: This detailed project report.

demo.png: A folder containing usage demos of the tool.
