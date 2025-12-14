import argparse

from src.fetcher import fetch_posts, save_posts
from src.log_generator import generate_logs
from src.report import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Log Analiz Projesi – API'den veri çekme, log üretme ve analiz"
    )

    parser.add_argument(
        "--fetch",
        action="store_true",
        help="API'den postları çek ve raw_posts.json dosyasını güncelle",
    )

    parser.add_argument(
        "--generate",
        action="store_true",
        help="raw_posts.json dosyasından log üret ve app.log oluştur",
    )

    parser.add_argument(
        "--analyze",
        action="store_true",
        help="app.log dosyasını analiz et ve raporları oluştur",
    )

    args = parser.parse_args()

    if args.fetch:
        posts = fetch_posts()
        if posts:
            save_posts(posts)

    if args.generate:
        generate_logs()

    if args.analyze:
        generate_report()

    if not (args.fetch or args.generate or args.analyze):
        parser.print_help()


if __name__ == "__main__":
    main()
