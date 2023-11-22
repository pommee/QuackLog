import datetime
from fastapi.responses import JSONResponse
import uvicorn

from fastapi import FastAPI, HTTPException, Request
from core.database.logs import save_log, get_logs_from_range

app = FastAPI()


def start():
    uvicorn.run("core.v1.api:app", host="0.0.0.0", port=8000, reload=False)


@app.post("/")
def create_log_item(request: Request):
    log_item = request.json()
    save_log(log_item)


@app.get("/")
def get_logs_within_range(request: Request):
    print("test")
    start_param = request.query_params.get("start")
    end_param = request.query_params.get("end")

    missing_params = [
        param
        for param, value in {"start": start_param, "end": end_param}.items()
        if not value
    ]

    if missing_params:
        error_data = {
            "status_code": 400,
            "message": "Missing parameter(s)",
            "parameters": missing_params,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        return JSONResponse(content=error_data, status_code=400)

    try:
        start_date, end_date = map(
            datetime.datetime.fromisoformat, [start_param, end_param]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid datetime format")

    return get_logs_from_range(start_date, end_date)
