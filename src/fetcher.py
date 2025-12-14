import requests
import json
from pathlib import Path

API_URL = "https://jsonplaceholder.typicode.com/posts"
DATA_PATH = Path("data/raw_posts.json")


def fetch_posts(limit: int = 100) -> list[dict]:
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        posts = response.json()

        if not isinstance(posts, list):
            raise ValueError("Beklenmeyen veri formatı")

        return posts[:limit]

    except requests.exceptions.Timeout:
        print("⏱️ Zaman aşımı oluştu. İnternet bağlantınızı kontrol edin.")
    except requests.exceptions.HTTPError as e:
        print(f"🌐 HTTP hatası: {e}")
    except requests.exceptions.RequestException as e:
        print(f"🚫 Ağ hatası: {e}")
    except ValueError as e:
        print(f"❌ Veri hatası: {e}")

    return []


def save_posts(posts: list[dict]):
    try:
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)

        print(f"✅ {len(posts)} kayıt kaydedildi → {DATA_PATH}")

    except OSError as e:
        print(f"💾 Dosya yazma hatası: {e}")


if __name__ == "__main__":
    posts = fetch_posts()

    if posts:
        save_posts(posts)
