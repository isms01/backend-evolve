import os
import re
from datetime import date
from pathlib import Path

PROGRESS_LOG_PATH = "progress-log.md"
LEETCODE_DIR = ["leetcode/easy", "leetcode/medium", "leetcode/hard"]


def extract_number_and_title(filename: str):
    match = re.match(r"(\d+)_([a-z0-9_]+)\.py", filename)
    if match:
        number = int(match.group(1))
        title = match.group(2).replace("_", " ").title()
        return number, title
    return None, None


def format_entry(number: int, title: str):
    return f"- ✅ Solved LeetCode #{number}: {title} – Added via GitHub Actions."


def main():
    today = date.today().isoformat()
    new_entries = []

    # Get existing log content
    if not os.path.exists(PROGRESS_LOG_PATH):
        with open(PROGRESS_LOG_PATH, "w") as f:
            f.write("# Progress Log\n")

    with open(PROGRESS_LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Check which problems are already logged
    logged_problems = set()
    for line in lines:
        match = re.search(r"LeetCode #(\d+):", line)
        if match:
            logged_problems.add(int(match.group(1)))

    # Scan leetcode files and find new ones
    for dir_name in LEETCODE_DIR:
        if not Path(dir_name).is_dir():
            continue
        for file_path in Path(dir_name).glob("*.py"):
            number, title = extract_number_and_title(file_path.name)
            if number and number not in logged_problems:
                new_entries.append((number, title))

    if not new_entries:
        print("✅ No new problems to add.")
        return

    # Create new log block
    log_block = [f"## **{today}**\n", "\n", "### 🧠 LeetCode\n"]
    for number, title in sorted(new_entries):
        log_block.append(format_entry(number, title) + "\n")
    log_block.append("\n\n")

    # Insert new block after "# Progress Log"
    for i, line in enumerate(lines):
        if line.strip() == "# Progress Log":
            insert_index = i + 1
            break
    else:
        insert_index = 0  # fallback

    updated_lines = lines[:insert_index] + log_block + lines[insert_index:]

    with open(PROGRESS_LOG_PATH, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

    print(f"📝 Inserted {len(new_entries)} new entries for {today}.")


if __name__ == "__main__":
    main()
