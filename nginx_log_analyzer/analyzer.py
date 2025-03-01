from statistics import mean, median
from typing import List

from .models import LogEntry


def generate_report(logs: List[LogEntry]) -> dict:
    response_times = [log.response_time for log in logs]
    return {
        "total_requests": len(logs),
        "average_response_time": mean(response_times),
        "median_response_time": median(response_times),
        "unique_ips": len(set(log.ip for log in logs)),
    }
