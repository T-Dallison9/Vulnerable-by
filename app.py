# ------------------------------------------------------------
# app_secure.py
# SECURE VERSION OF APPLICATION
# ------------------------------------------------------------

import hashlib
import secrets
import subprocess
import os
import tempfile


# ------------------------------------------------------------
# Secure way: Use environment variable for password
# ------------------------------------------------------------
DB_PASSWORD = os.getenv("DB_PASSWORD")

if DB_PASSWORD is None:
    raise ValueError("Database password not set in environment variables")


# ------------------------------------------------------------
# No hardcoded default password
# ------------------------------------------------------------
def authenticate(user, password):
    if password == DB_PASSWORD:
        print("Authenticated")
    else:
        print("Access denied")


# ------------------------------------------------------------
# Strong cryptographic hash (SHA-256 instead of MD5)
# ------------------------------------------------------------
def secure_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


# ------------------------------------------------------------
# Secure random token generator
# ------------------------------------------------------------
def secure_token():
    return secrets.token_hex(16)


# ------------------------------------------------------------
# Safe subprocess usage (no shell=True)
# ------------------------------------------------------------
def safe_command(cmd_list):
    subprocess.run(cmd_list, check=True)


# ------------------------------------------------------------
# Secure temporary file handling
# ------------------------------------------------------------
def create_temp_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"Temporary data")
        return tmp.name


# ------------------------------------------------------------
# Execute secure code
# ------------------------------------------------------------
if __name__ == "__main__":
    authenticate("admin", DB_PASSWORD)
    print(secure_hash(DB_PASSWORD))
    print(secure_token())
    safe_command(["echo", "Bandit secure test"])
    print("Temporary file created at:", create_temp_file())
