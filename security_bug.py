# Hardcoded password - security issue!
PASSWORD = "admin123"

def unsafe_sql(user_input):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query

def divide(a, b):
    # No zero division check
    return a / b
```

9. **Scroll to bottom and click "Commit changes"**
   - It will commit directly to `add-buggy-code` branch ✅

---

### **Step 3: Create the Pull Request**

10. **GitHub will show a yellow banner** at the top saying:
```
    add-buggy-code had recent pushes
    [Compare & pull request] button
```

11. **Click "Compare & pull request"**

12. **On the next page:**
    - Title: "Add buggy code for AI review"
    - Click **"Create pull request"**

✅ **Done! PR created!**

---

## 📊 **What Should Happen:**

**Terminal 1 (Backend) should show:**
```
📥 Webhook received from GitHub
✅ Webhook signature verified
🔍 DEBUG - Webhook Action: opened
🔍 DEBUG - Event Keys: [...]
🔍 DEBUG - Has pull_request? True
📋 PR Data: {...}
🔍 Processing PR #1 - Action: opened
🤖 Starting AI code review...
