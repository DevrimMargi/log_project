import csv
import json
from collections import defaultdict, Counter
from pathlib import Path

from src.parser import parse_log_line

LOG_PATH = Path("data/app.log")
REPORT_DIR = Path("reports")


def generate_report():
    records = []

    with open(LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            record = parse_log_line(line)
            if record:
                records.append(record)

    total_logs = len(records)

    level_counts = Counter(r.level for r in records)

    by_user = defaultdict(lambda: {"total": 0, "errors": 0})
    for r in records:
        by_user[str(r.user_id)]["total"] += 1
        if r.is_error:
            by_user[str(r.user_id)]["errors"] += 1

    error_messages = [
        r.message for r in records if r.is_error
    ]
    top_error_messages = sorted(
        error_messages, key=len, reverse=True
    )[:5]

    REPORT_DIR.mkdir(exist_ok=True)

    # CSV
    with open(REPORT_DIR / "summary.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["level", "count"])
        for level, count in level_counts.items():
            writer.writerow([level, count])

    # JSON
    summary = {
        "total_logs": total_logs,
        "by_level": dict(level_counts),
        "by_user": by_user,
        "top_error_messages": top_error_messages,
    }

    with open(REPORT_DIR / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("✅ Raporlar oluşturuldu → reports/")


if __name__ == "__main__":
    generate_report()
