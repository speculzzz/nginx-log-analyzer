from datetime import datetime

from .models import LogEntry


def parse_log_file(file_path: str) -> list[LogEntry]:
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 10:
                log = LogEntry(
                    ip=parts[0],
                    time=datetime.strptime(parts[3][1:], "%d/%b/%Y:%H:%M:%S"),
                    method=parts[5][1:],
                    url=parts[6],
                    status=int(parts[8]),
                    response_time=float(parts[-1]),
                )
                logs.append(log)
    return logs
