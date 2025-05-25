import os


def main():
    app_env = os.environ.get("APP_ENV", "production")
    print(f"Hello, Docker! Running in {app_env} mode.")


if __name__ == "__main__":
    main()
