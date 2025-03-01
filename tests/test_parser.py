from nginx_log_analyzer import parse_log_file


def test_parse_log_file():
    logs = parse_log_file("logs/access.log")
    assert len(logs) > 0
    assert hasattr(logs[0], "ip")
    assert hasattr(logs[0], "response_time")
