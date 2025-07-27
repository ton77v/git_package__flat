from git_package.src.app import start_app
from git_package.src.db.db import init_db

# from git_package import start_app, init_db


def start_dev() -> int:
    print("starting the server...")
    init_db()
    start_app(debug_mode=True)
    return 0


if __name__ == "__main__":
    exit(start_dev())