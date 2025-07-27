from app import start_app


def start_dev() -> int:
    print("starting the server...")
    start_app(debug_mode=True)
    return 0


if __name__ == "__main__":
    exit(start_dev())