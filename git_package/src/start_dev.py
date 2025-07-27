from app import start_app
from db.db import init_db


def start_dev() -> int:
    print("starting the server...")
    init_db()
    start_app(debug_mode=True)
    return 0


if __name__ == "__main__":
    exit(start_dev())