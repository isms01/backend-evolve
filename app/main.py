# app/main.py
from app.scheduler import Scheduler


def main():
    scheduler = Scheduler()
    while True:
        try:
            user_input = input(
                "Enter your scheduler(Ex. '2023-10-01 Meeting with Bob '):\n>"
            )
        except EOFError:
            print("\n Exit triggered (EOF). Exiting gracefully...")
            break

        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            date, description = user_input.split(" ", 1)
            scheduler.add_event(date, description)
        except ValueError:
            print("Please enter the date and description separated by a space.")
    scheduler.list_events()


if __name__ == "__main__":
    main()
