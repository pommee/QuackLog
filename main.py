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
    return get_logs_from_range(
        start_year,
        start_month,
        start_day,
        end_year,
        end_month,
        end_day,
    )
