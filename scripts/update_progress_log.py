import datetime
import os
from pathlib import Path

LEETCODE_ROOT = Path("leetcode")
PROGRESS_LOG = Path("progress-log.md")


def extract_info(filepath: Path):
    number_str, rest = filepath.stem.split("_", 1)
    number = int(number_str)
    title = rest.replace("_", " ").title()
    return number, title


def find_today_files():
    today = datetime.date.today()
    changed = []
    for category in ["easy", "medium", "hard"]:
        dir_path = LEETCODE_ROOT / category
        if not dir_path.exists():
            continue
        for file in dir_path.glob("*.py"):
            mtime = datetime.date.fromtimestamp(file.stat().st_mtime)
            if mtime == today:
                changed.append(file)
    return changed


def update_progress_log():
    today_str = datetime.date.today().isoformat()
    header = f"## **{today_str}**\n\n"
    leetcode_section = "### 🧠 LeetCode\n"

    updated_files = find_today_files()
    if not updated_files:
        print("No updated LeetCode files today.")
        return

    entries = []
    for file in sorted(updated_files):
        number, title = extract_info(file)
        entries.append(
            f"- ✅ Solved LeetCode #{number:04d}: {title}\n  - Added via GitHub Actions."
        )
    log_block = header + leetcode_section + "\n".join(entries) + "\n\n"
    with open(PROGRESS_LOG, "a", encoding="utf-8") as f:
        f.write(log_block)


if __name__ == "__main__":
    update_progress_log()
