from typing import Dict
import json as _json
import datetime as _dt


def get_all_events() -> Dict:
    with open("events.json") as events_file:
        data = _json.load(events_file)

    return data


def todays_events() -> Dict:
    today = _dt.date.today()
    month = today.strftime("%B").lower()
    day = str(today.day)
    events = get_all_events()
    return events[month][day]


def month_events(month: str) -> Dict:
    events = get_all_events()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "this month isn't real you fool"


def day_events(month: str, day: int) -> Dict:
    events = get_all_events()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "you did something stupid"