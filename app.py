import pycron, os
from datetime import datetime
from fastapi import FastAPI, HTTPException

CRASH_SCHEDULE = os.getenv("CRASH_SCHEDULE", "* * * * *")

app = FastAPI(
    title="Crashi",
    description="A simple API for returning internal server errors on a schedule for reliability testing.",
    version="v0.1",
)

@app.get("/api/health")
async def health():
    if pycron.is_now(CRASH_SCHEDULE):
        raise HTTPException(
            status_code=500,
            detail=f"This internal server error at {datetime.now()} is expected as the request is within the crash schedule: '{CRASH_SCHEDULE}'"
        )
    else:
        return {
            "message": "OK",
            "detail": f"{datetime.now()} is not within the crash schedule '{CRASH_SCHEDULE}'"
        }