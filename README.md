Task 10: Password Strength Analyzer
This project is a command-line tool built in Python to evaluate the strength of a given password based on common complexity rules.

Objective
The goal of this task was to build a functional password analyzer to gain a practical understanding of what constitutes a strong password. This exercise helps demonstrate key concepts in cyber hygiene, password policies, and basic input validation.

Tools Used
Python 3: The programming language used to build the script.

VS Code / Kali Linux Terminal: For code development and execution.

How the Tool Works & Demonstration
The script (password_checker.py) prompts a user to enter a password and analyzes it against the following criteria:

Length: Checks if the password is at least 8 characters long.

Character Variety: Checks for the presence of:

Uppercase letters (A-Z)

Lowercase letters (a-z)

Numbers (0-9)

Special characters (!@#$%)

Based on the results, the tool provides a strength rating (Weak, Medium, or Strong) and a list of specific recommendations for improvement. The screenshots in the screenshots folder demonstrate the tool analyzing passwords of varying complexity.

Files in Repository
password_checker.py: The Python source code for the tool.

README.md: This summary file.

demo.png: A folder containing usage demos of the tool analyzing weak, medium, and strong passwords.
