from fastapi import FastAPI, Request
from db_helper import save_log, get_logs_from_range

app = FastAPI()

@app.post("/")
async def create_log_item(request: Request):
    log_item = await request.json()
    save_log(log_item)


@app.get("/")
async def get_logs_within_range(
    start_year: str,
    start_month: str,
    start_day: str,
    end_year: str,
    end_month: str,
    end_day: str,
):
    logs = []

    # Iterate through the range of dates and retrieve logs
    current_year, current_month, current_day = start_year, start_month, start_day
    while current_year <= end_year:
        while current_month <= "12" if current_year != end_year else end_month:
            while current_day <= "31" if current_month != end_month else end_day:
                test = get_logs_from_range(current_year, current_month, current_day)
                print(test)
                logs.extend(get_logs_from_range(current_year, current_month, current_day))
                current_day = str(int(current_day) + 1).zfill(2)
            current_day = "01"
            current_month = str(int(current_month) + 1).zfill(2)
        current_month = "01"
        current_year = str(int(current_year) + 1)

    if not logs:
        raise HTTPException(status_code=404, detail="Logs not found")

    return logs