# CYBERGUARD v1.0
### Personal Account Security Monitoring System

## Project Overview

CYBERGUARD is a beginner-friendly Python-based cybersecurity simulation designed to monitor account information, analyse login activity, identify potential security threats, and generate a security report.

The project simulates the work of a junior cybersecurity analyst by assessing account security conditions using basic Python programming concepts.

## Project Objectives

- Collect basic user account information.
- Monitor failed login attempts.
- Identify potentially suspicious account activity.
- Check whether an account is active or inactive.
- Assess password strength.
- Generate a security report with appropriate recommendations.

## Features

**1. User Information Collection**

Collects username, email address, password, age, IP address, failed login attempts, and account status.

**2. Security Threat Detection**

Analyses failed login attempts and identifies potential brute-force attacks.

**3. Account Status Monitoring**

Checks whether an account is active or inactive.

**4. Password Strength Checker**

Assesses password strength based on its length.

- Fewer than 8 characters: Weak.
- 8–11 characters: Moderate.
- 12 or more characters: Strong.

**5. Security Analyst Report**

Generates a report containing account information, password assessment, detected threats, final security status, and recommendations.

## Technologies Used

- Python 3
- Visual Studio Code
- GitHub

## Python Concepts Demonstrated

- Variables and data types.
- Strings, integers and Booleans.
- Input and output using `input()` and `print()`.
- Type conversion using `int()`.
- Data type verification using `type()`.
- Comparison and assignment operators.
- Conditional statements (`if`, `elif`, and `else`).

## How to Run the Project

1. Install Python 3 on your computer.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Run the following command:

```bash
python cyberguard.py
```

6. Enter the requested account information.
7. View the generated security report.

## Testing

The system is tested using three scenarios:

- Normal account: No failed login attempts.
- Suspicious account: Seven failed login attempts.
- Disabled account: An inactive account with failed login attempts.

## Project Limitations

CYBERGUARD is an educational cybersecurity simulation. It does not connect to real user accounts, monitor actual network traffic, or detect real-world attacks.

The password assessment is based only on password length and is not a complete password security assessment.

## Author

**Akoto123dot**

## Project Type

Individual Beginner Python Cybersecurity Project.
