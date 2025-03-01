from fastapi import FastAPI, HTTPException

from .analyzer import generate_report
from .parser import parse_log_file

app = FastAPI()


@app.get("/report")
def get_report():
    try:
        logs = parse_log_file("logs/access.log")
        report = generate_report(logs)
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def run_server():
    """Start the server using uvicorn."""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
