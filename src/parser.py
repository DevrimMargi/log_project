import re
from datetime import datetime
from src.models import LogRecord

LOG_PATTERN = re.compile(
    r"""
    ^\[
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})
    \]\s
    (?P<level>INFO|WARNING|ERROR)\s
    \(user_id=(?P<user_id>\d+),\spost_id=(?P<post_id>\d+)\):
    \s
    (?P<message>.+)
    $
    """,
    re.VERBOSE,
)


def parse_log_line(line: str):
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    return LogRecord(
        timestamp=datetime.strptime(
            match.group("timestamp"), "%Y-%m-%d %H:%M:%S"
        ),
        level=match.group("level"),
        user_id=int(match.group("user_id")),
        post_id=int(match.group("post_id")),
        message=match.group("message"),
    )
