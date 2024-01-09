import uvicorn

from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException, Request
from core.database.logs import save_log, get_logs_from_range

api = FastAPI()


def start():
    uvicorn.run("core.v1.api:api", host="0.0.0.0", port=8000, reload=False)


@api.post("/")
async def create_log_item(request: Request):
    return save_log(await request.json())


@api.get("/")
def get_logs_within_range(request: Request):
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
            "timestamp": datetime.now().isoformat(),
        }
        return JSONResponse(content=error_data, status_code=400)

    try:
        start_date, end_date = map(
            datetime.now().fromisoformat, [start_param, end_param]
        )
        return get_logs_from_range(start_date, end_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format")
