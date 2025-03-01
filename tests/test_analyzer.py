from datetime import datetime

from pytest import approx

from nginx_log_analyzer import LogEntry, generate_report


def test_generate_report():
    logs = [
        LogEntry(
            ip="127.0.0.1",
            time=datetime.now(),
            method="GET",
            url="/",
            status=200,
            response_time=0.1,
        ),
        LogEntry(
            ip="127.0.0.2",
            time=datetime.now(),
            method="POST",
            url="/submit",
            status=200,
            response_time=0.2,
        ),
    ]
    report = generate_report(logs)
    assert report["total_requests"] == 2
    assert report["average_response_time"] == approx(0.15)
