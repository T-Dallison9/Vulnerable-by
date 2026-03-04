# ------------------------------------------------------------
# app.py
# VULNERABLE APPLICATION
# Used to validate Bandit GitHub Actions workflow
# ------------------------------------------------------------

import hashlib
import random
import subprocess
import os
import tempfile

# ------------------------------------------------------------
# B105 – Hardcoded password (MEDIUM)
# ------------------------------------------------------------
DB_PASSWORD = "admin123"

# ------------------------------------------------------------
# B107 – Hardcoded default password argument (MEDIUM)
# ------------------------------------------------------------
def authenticate(user, password="password"):
    if password == DB_PASSWORD:
        print("Authenticated")
    else:
        print("Access denied")

# ------------------------------------------------------------
# B303 – Weak cryptographic hash (MD5) (MEDIUM)
# ------------------------------------------------------------
def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

# ------------------------------------------------------------
# B311 – Insecure random for security purposes (LOW)
# ------------------------------------------------------------
def insecure_token():
    return random.random()

# ------------------------------------------------------------
# B602 – subprocess with shell=True (HIGH)
# ------------------------------------------------------------
def dangerous_command(cmd):
    subprocess.call(cmd, shell=True)

# ------------------------------------------------------------
# B108 – Hardcoded temporary file path (LOW)
# ------------------------------------------------------------
temp_path = "/tmp/app_temp_file.txt"

# ------------------------------------------------------------
# Execute vulnerable code
# ------------------------------------------------------------
if __name__ == "__main__":
    authenticate("admin")
    print(weak_hash(DB_PASSWORD))
    print(insecure_token())
    dangerous_command("echo Bandit test")
