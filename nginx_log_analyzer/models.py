from datetime import datetime

from pydantic import BaseModel


class LogEntry(BaseModel):
    ip: str
    time: datetime
    method: str
    url: str
    status: int
    response_time: float
