# 🧠 LeetCode Submissions Downloader & Organizer

This Python script allows you to **automatically fetch all your accepted LeetCode submissions** (filtered by language) and **save them locally** in a structured format. It's ideal for those who want to maintain a GitHub repository of their problem-solving journey on LeetCode.

---

## 🚀 Features

- ✅ Automatically fetches all **accepted submissions**
- 🗂 Saves code in `.java`, `.py`, or `.cpp` format (based on selected language)
- 🧾 Avoids duplicate saves
- 📄 Saves each file as `Problem_Name.java` with the title as a comment
- 🔐 Authenticates securely using your **browser session cookies**
- 🕸 Handles API pagination to fetch **all submissions**, not just recent ones

---

## ⚙️ Requirements

- Python 3.x
- Install dependencies:
  ```bash
  pip install requests tqdm

🛠 Setup Instructions
Log into LeetCode in your browser.

Get cookies:

Open Developer Tools (F12 or Ctrl+Shift+I)

Go to Application > Cookies > https://leetcode.com

Copy the values of:

LEETCODE_SESSION

csrftoken


Update the script: Replace the following lines with your copied cookie values:
LEETCODE_SESSION = "your_LEETCODE_SESSION_cookie"
CSRF_TOKEN = "your_csrftoken_cookie"
Choose language to filter (e.g., "java", "python", "cpp"):
LANGUAGE = "java"
Run the script:
python leetcode_scraper.py


All accepted solutions will be saved in the LeetCode-Solutions folder




