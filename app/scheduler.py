# app/scheduler.py


class Scheduler:
    def __init__(self):
        self.events = []

    def add_event(self, date: str, description: str):
        event = {"date": date, "description": description}
        self.events.append(event)
        print(f"Event added: {event}")

    def list_events(self):
        if not self.events:
            print("No events scheduled.")
            return
        print("Scheduled events:")
        for i, event in enumerate(self.events, 1):
            print(f"{i}. {event['date']}-{event['description']}")
