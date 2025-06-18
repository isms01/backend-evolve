from datetime import datetime
from pathlib import Path

LEETCODE_ROOT = Path("leetcode")
PROGRESS_LOG = Path("progress-log.md")


def extract_info(file_path: Path):
    parts = file_path.stem.split("_", 1)
    number = parts[0].lstrip("0")
    title = parts[1].replace("_", " ").title() if len(parts) > 1 else "Unknown"
    return number, title


def find_today_files():
    today = datetime.now().date()
    changed = []
    for category in ["easy", "medium", "hard"]:
        for file in (LEETCODE_ROOT / category).glob("*.py"):
            if datetime.fromtimestamp(file.stat().st_mtime).date() == today:
                changed.append(file)
    return changed


def update_progress_log():
    today_str = datetime.now().date().isoformat()
    header = f"## {today_str}"
    leetcode_section = "### 🧠 LeetCode"

    updated_files = find_today_files()
    if not updated_files:
        print("No updated LeetCode files today.")
        return

    entries = []
    for file in sorted(updated_files):
        number, title = extract_info(file)
        entries.append(
            f"- ✅ Solved LeetCode #{number}: {title} – Added via GitHub Actions."
        )

    log_block = header + "\n\n" + leetcode_section + "\n" + "\n".join(entries) + "\n\n"

    with open(PROGRESS_LOG, "r", encoding="utf-8") as f:
        current_log = f.read()

    with open(PROGRESS_LOG, "w", encoding="utf-8") as f:
        f.write(log_block + current_log)


if __name__ == "__main__":
    update_progress_log()
