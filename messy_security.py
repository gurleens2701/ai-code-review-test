import os
import sqlite3

# ISSUE 1: Hardcoded secrets (critical security issue!)
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_PASSWORD = "admin123"
API_TOKEN = "sk-proj-1234567890abcdefghijklmnop"

# ISSUE 2: SQL Injection vulnerability
def get_user_by_name(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Dangerous! User input directly in query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# ISSUE 3: No error handling - will crash!
def divide_numbers(a, b):
    return a / b  # What if b is 0?

def read_config(filename):
    file = open(filename)  # File never closed! Memory leak
    return file.read()

# ISSUE 4: Using eval() - extremely dangerous!
def calculate_expression(user_input):
    # User can execute ANY Python code!
    result = eval(user_input)
    return result

# ISSUE 5: Path traversal vulnerability
def get_user_file(username, filename):
    # User could access any file: "../../../etc/passwd"
    path = "/home/users/" + username + "/" + filename
    with open(path) as f:
        return f.read()

# ISSUE 6: Weak cryptography
def hash_password(password):
    import hashlib
    # MD5 is broken! Should use bcrypt or argon2
    return hashlib.md5(password.encode()).hexdigest()

# ISSUE 7: Race condition
balance = 1000
def withdraw(amount):
    global balance
    if balance >= amount:  # Not thread-safe!
        balance -= amount
        return True
    return False

# ISSUE 8: No input validation
def send_email(email, message):
    # No validation - could be used for email injection
    os.system(f"sendmail {email} < {message}")

# ISSUE 9: Infinite loop risk
def process_items(items):
    i = 0
    while i < len(items):
        print(items[i])
        # BUG: forgot to increment i!

# ISSUE 10: Missing authentication
def delete_user_account(user_id):
    # No auth check - anyone can delete any account!
    conn = sqlite3.connect('users.db')
    conn.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()

# ISSUE 11: Exposing sensitive info in logs
def login_user(username, password):
    print(f"Login attempt: username={username}, password={password}")  # BAD!
    # Rest of login logic...

# ISSUE 12: No rate limiting
def api_endpoint(request):
    # Can be abused for DDoS
    expensive_operation()
    return "OK"

def expensive_operation():
    # Simulate heavy computation
    for i in range(1000000):
        x = i ** 2
```

8. **Commit the file** (it will commit to `security-issues-test` branch)

---

### **Step 3: Create Pull Request**

9. **GitHub shows yellow banner** → Click **"Compare & pull request"**

10. **Title:** `Add security test code - DO NOT MERGE`

11. **Description:**
```
Testing AI code review system with intentionally vulnerable code.

Expected issues:
- Hardcoded secrets
- SQL injection
- No error handling
- Use of eval()
- Path traversal
- Weak crypto
- And more...
```

12. **Click "Create pull request"**

**🚨 DO NOT MERGE THIS PR! 🚨**

---

## 📊 **Watch the Magic!**

### **Terminal 1 (Backend) Should Show:**
```
📥 Webhook received from GitHub
✅ Webhook signature verified
🔍 Processing PR #X - Action: opened
📄 Fetched diff: ... characters
🤖 Starting AI code review...
✅ AI review completed: ❌ Changes need attention - critical issues found
💬 Created X inline comments
✅ Review posted to GitHub successfully!
