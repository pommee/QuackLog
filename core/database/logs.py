import datetime
import json

from fastapi import HTTPException


def save_log(log_item):
    time_sent = log_item.get("time_sent")
    if time_sent:
        date_parts = time_sent.split("T")[0].split("-")
        year, month, day = date_parts

        try:
            with open("logs_main.json", "r") as infile:
                content = infile.read()
                if content:
                    content = json.loads(content)
                else:
                    content = {}
        except FileNotFoundError:
            content = {}

        content.setdefault("logs", {})
        content["logs"].setdefault(year, {})
        content["logs"][year].setdefault(month, {})
        content["logs"][year][month].setdefault(day, [])

        content["logs"][year][month][day].append(log_item)

        with open("logs_main.json", "w") as outfile:
            json.dump(content, outfile, indent=2)

        return {"message": "Data appended successfully"}
    else:
        return {"error": "Invalid log format. 'time_sent' field is missing or invalid."}


def get_logs_from_range(start_date: datetime, end_date: datetime):
    end_date += datetime.timedelta(days=1)
    logs = []

    current_date = start_date
    while current_date < end_date:
        year, month, day = (
            current_date.strftime("%Y"),
            current_date.strftime("%m"),
            current_date.strftime("%d"),
        )
        logs.extend(get_logs_from_range_helper(year, month, day))
        current_date += datetime.timedelta(days=1)

    if not logs:
        raise HTTPException(status_code=404, detail="Logs not found")

    return logs


def get_logs_from_range_helper(year: str, month: str, day: str) -> dict:
    try:
        with open("logs_main.json", "r") as infile:
            content = json.load(infile)
            logs = content.get("logs", {})
            return logs.get(year, {}).get(month, {}).get(day, [])
    except FileNotFoundError:
        return []
