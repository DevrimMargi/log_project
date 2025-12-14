from src.parser import parse_log_line


def test_parse_log_line():
    line = "[2025-12-14 13:15:56] ERROR (user_id=10, post_id=91): aut amet sed"
    record = parse_log_line(line)

    assert record is not None
    assert record.level == "ERROR"
    assert record.user_id == 10
    assert record.post_id == 91
    assert record.is_error is True
