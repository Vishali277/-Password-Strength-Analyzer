Task 10: Password Strength Checker
This project is a simple command-line tool written in Python to check how strong a password is.

Objective
The goal of this task was to build a tool that can analyze a password and give feedback on its strength. This helps in understanding what makes a good password and why security policies (like forcing users to add numbers and symbols) exist.

How the Tool Works
The Python script (password_checker.py) asks the user to enter a password. It then checks the password against a few common rules:

Length: Is it at least 8 characters long?

Uppercase: Does it have at least one uppercase letter (A-Z)?

Lowercase: Does it have at least one lowercase letter (a-z)?

Numbers: Does it have at least one number (0-9)?

Special Characters: Does it have at least one special character (like !, @, #, $)?

Based on how many rules the password follows, the tool gives it a score and rates it as Weak, Medium, or Strong. It also prints a list of recommendations for any rules that were missed.

Demonstration
The screenshot below demonstrates the tool analyzing several passwords of varying complexity and providing feedback:

What I Learned
Why Complexity Matters: I learned that adding just one different type of character (like a number or a symbol) makes a password much harder for an attacker to guess or "brute-force."

The Importance of Length: A short password, even if it's complex, can be cracked much faster than a long one. Length is one of the most important factors for password security.

Basic Python for Security: This task was a good way to see how simple programming can be used to build useful security tools and to understand concepts like input validation.

Files in This Repository
password_checker.py: The Python source code for the tool.

README.md: This file.

demo.png: The screenshot showing the tool in action.
