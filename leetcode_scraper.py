import requests
import os
import time
from tqdm import tqdm

# Replace these with your copied cookie values
LEETCODE_SESSION = "Session Code goes here "
CSRF_TOKEN = "CSRF token goes here"
LANGUAGE = "java"

SAVE_DIR = "LeetCode-Solutions"
os.makedirs(SAVE_DIR, exist_ok=True)

session = requests.Session()
session.cookies.set("LEETCODE_SESSION", LEETCODE_SESSION)
session.cookies.set("csrftoken", CSRF_TOKEN)

headers = {
    'Referer': 'https://leetcode.com',
    'User-Agent': 'Mozilla/5.0',
    'x-csrftoken': CSRF_TOKEN
}

print("📥 Fetching all submissions from LeetCode...")

submissions_url = "https://leetcode.com/api/submissions/"
offset = 0
limit = 50  # Max allowed by LeetCode
all_submissions = []

while True:
    try:
        resp = session.get(f"{submissions_url}?offset={offset}&limit={limit}", headers=headers)

        if resp.status_code != 200:
            print(f"⚠️ Error {resp.status_code} at offset {offset}. Retrying in 5 seconds...")
            time.sleep(5)
            continue

        data = resp.json()
        submissions = data.get('submissions_dump', [])
        all_submissions.extend(submissions)

        print(f"📄 Fetched {len(submissions)} submissions (Total: {len(all_submissions)})")

        if not data.get('has_next', False):
            break

        offset += limit
        time.sleep(1)  # be nice to the API

    except Exception as e:
        print(f"❌ Exception: {e}")
        break

print(f"✅ Total submissions fetched: {len(all_submissions)}")

# Save accepted ones
count = 0
for submission in tqdm(all_submissions, desc="💾 Saving accepted solutions"):
    if submission['status_display'] != 'Accepted':
        continue
    if submission['lang'].lower() != LANGUAGE:
        continue

    title = submission['title'].replace(" ", "_").replace("?", "").replace("/", "_")
    code = submission['code']
    ext = {
        "python": "py",
        "java": "java",
        "cpp": "cpp"
    }.get(LANGUAGE, "txt")

    filename = os.path.join(SAVE_DIR, f"{title}.{ext}")
    
    # Avoid duplicates
    if os.path.exists(filename):
        continue

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"// {submission['title']}\n")
        f.write(code)

    count += 1

print(f"🎉 Saved {count} accepted {LANGUAGE} solutions to `{SAVE_DIR}/`")
