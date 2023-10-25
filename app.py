import pycron, os, logging
from datetime import datetime
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


CRASH_SCHEDULE = os.getenv("CRASH_SCHEDULE", "* * * * *")
SIM_ENV_MISSING = os.getenv("SIM_ENV_MISSING", "NO")
SIM_HIDDEN_ENV_MISSING = os.getenv("SIM_HIDDEN_ENV_MISSING", "NO")

logger = logging.getLogger(__name__)
logger.info(f"Crash schedule set to: {CRASH_SCHEDULE}\nSimulating missing env crash: {SIM_ENV_MISSING}\nSimulating hidden missing env: {SIM_HIDDEN_ENV_MISSING}")

if SIM_ENV_MISSING != "NO":
    logger.error(f"Set to simulate missing environment crash: {SIM_ENV_MISSING} - exiting app")

app = FastAPI(
    title="Crashi",
    description="A simple API for returning internal server errors on a schedule for reliability testing.",
    version="v0.1",
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
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

@app.get("/api/simenv")
async def sim_env():
    if SIM_HIDDEN_ENV_MISSING != "NO":
        raise HTTPException(
            status_code=500,
            detail=f"This internal server error at {datetime.now()} is expected as SIM_HIDDEN_ENV_MISSING is set to {SIM_HIDDEN_ENV_MISSING} indicating that a missing feature flag environment variable should be set."
        )
    else:
        return {
            "message": "OK",
            "detail": f"Not simulating a missing feature flag - returning OK"
        }

@app.api_route("/{path_name:path}", methods=["GET"])
async def catch_all(request: Request, path_name: str):
    logger.info(f"Catch all request: {request} with path {path_name}")
    return await sim_env()