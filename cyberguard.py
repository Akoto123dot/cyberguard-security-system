#CYBERGUARD v1.0 PERSONAL SECURITY MONITORING SYSTEM

print("========================================")
print("           CYBERGUARD v1.0")
print("    PERSONAL SECURITY MONITORING SYSTEM")
print("========================================")

print()
print("Welcome, Security Analyst!")
print()
print("Your mission is to monitor account")
print("information and identify potential threats.")
print()
print("Starting security assessment...")

#USER INFORMATION COLLECTION

print()
print("========================================")
print("         USER INFORMATION")
print("========================================")

username = input("Enter username: ")

email = input("Enter email address: ")

password = input("Enter password: ")

age = int(input("Enter age: "))

ip_address = input("Enter IP address: ")

failed_attempts = int(input("Enter failed login attempts: "))

status = input("Is the account Active or Inactive? ")

if status == "Active":
    account_status = True
else:
    account_status = False

# DATA TYPE VERIFICATION

print()
print("========================================")
print("         DATA TYPE VERIFICATION")
print("========================================")

print("Username:", type(username))
print("Email:", type(email))
print("Password:", type(password))
print("Age:", type(age))
print("IP Address:", type(ip_address))
print("Failed Attempts:", type(failed_attempts))
print("Account Status:", type(account_status))

#PASSWORD STRENGTH CHECKER

password_length = len(password)

if password_length < 8:
    password_strength = "WEAK"
elif password_length <= 11:
    password_strength = "MODERATE"
else:
    password_strength = "STRONG"

#SECURITY THREAT DETECTION

if failed_attempts == 0:
    login_message = "No failed login attempts detected."

elif failed_attempts < 5:
    login_message = "Low security alert: Failed login attempts detected."

else:
    login_message = "CRITICAL WARNING: Possible brute-force attack detected."

#CCOUNT STATUS CHECK

if account_status == False:
    account_message = "Account access is currently disabled."

else:
    if failed_attempts < 5:
        account_message = "No critical login threat detected."
    else:
        account_message = "Account requires immediate security investigation."

#FINAL THREAT ASSESSMENT

if account_status == False:
    threat_level = "ACCOUNT INACTIVE"
    recommendation = "Verify the account status before allowing access."

elif failed_attempts >= 5:
    threat_level = "HIGH"
    recommendation = "Investigate the login activity and secure the account immediately."

elif failed_attempts >= 1:
    threat_level = "LOW"
    recommendation = "Monitor the account for additional suspicious login attempts."

else:
    threat_level = "LOW"
    recommendation = "No immediate action required. Continue routine monitoring."

#SECURITY ANALYST REPORT

print()
print("========================================")
print("         CYBERGUARD SECURITY REPORT")
print("========================================")

print()
print("USER INFORMATION")
print("----------------------------------------")

print("Username:", username)
print("Email:", email)
print("Age:", age)
print("IP Address:", ip_address)

if account_status == True:
    print("Account Status: ACTIVE")
else:
    print("Account Status: INACTIVE")


print()
print("SECURITY ANALYSIS")
print("----------------------------------------")

print("Password Assessment:", password_strength)
print("Failed Login Attempts:", failed_attempts)

print()
print("THREAT DETECTION")
print("----------------------------------------")

print(login_message)
print(account_message)

if failed_attempts >= 5:
    print("[WARNING] Possible brute-force attack detected.")

if account_status == False:
    print("[WARNING] Account is inactive.")


print()
print("FINAL SECURITY STATUS")
print("----------------------------------------")

print("THREAT LEVEL:", threat_level)

print()
print("RECOMMENDATION:")
print(recommendation)

print()
print("========================================")
print("       END OF SECURITY REPORT")
print("========================================")