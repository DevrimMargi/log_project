import json
import random
from datetime import datetime
from pathlib import Path

RAW_DATA_PATH = Path("data/raw_posts.json")
LOG_PATH = Path("data/app.log")

LOG_LEVELS = ["INFO", "WARNING", "ERROR"]


def generate_log_line(post: dict) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(LOG_LEVELS)

    user_id = post.get("userId")
    post_id = post.get("id")

    message = post.get("title") or post.get("body", "")

    return f"[{timestamp}] {level} (user_id={user_id}, post_id={post_id}): {message}"


def generate_logs():
    try:
        with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
            posts = json.load(f)

        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(LOG_PATH, "w", encoding="utf-8") as log_file:
            for post in posts:
                line = generate_log_line(post)
                log_file.write(line + "\n")

        print(f"✅ {len(posts)} log satırı üretildi → {LOG_PATH}")

    except FileNotFoundError:
        print("❌ raw_posts.json bulunamadı. Önce fetch işlemini yapın.")
    except json.JSONDecodeError:
        print("❌ JSON dosyası bozuk.")
    except OSError as e:
        print(f"💾 Dosya hatası: {e}")


if __name__ == "__main__":
    generate_logs()
