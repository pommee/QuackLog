import json


def save_log(log_item):
    time_sent = log_item.get("time_sent")
    if time_sent:
        date_parts = time_sent.split("T")[0].split("-")
        year, month, day = date_parts

        # Check if the file exists and is not empty
        try:
            with open("logs_main.json", "r") as infile:
                content = infile.read()
                if content:
                    content = json.loads(content)
                else:
                    content = {}
        except FileNotFoundError:
            content = {}

        # Create logs structure if not present
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


def get_logs_from_range(year: str, month: str, day: str) -> dict:
    try:
        with open("logs_main.json", "r") as infile:
            content = json.load(infile)
            logs = content.get("logs", {})
            return logs.get(year, {}).get(month, {}).get(day, [])
    except FileNotFoundError:
        return []