import uvicorn
from fastapi import FastAPI, Request
from db_helper import save_log, get_logs_from_range

app = FastAPI()


def start():
    uvicorn.run(
        "core.v1.api:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )


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
