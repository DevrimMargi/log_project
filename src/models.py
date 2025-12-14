from datetime import datetime


class LogRecord:
    def __init__(
        self,
        timestamp: datetime,
        level: str,
        user_id: int,
        post_id: int,
        message: str,
    ):
        self.timestamp = timestamp
        self.level = level
        self.user_id = user_id
        self.post_id = post_id
        self.message = message

    @property
    def is_error(self) -> bool:
        return self.level == "ERROR"

    def __str__(self) -> str:
        return (
            f"[{self.timestamp}] {self.level} "
            f"(user_id={self.user_id}, post_id={self.post_id}): {self.message}"
        )

    def __repr__(self) -> str:
        return (
            f"LogRecord(timestamp={self.timestamp!r}, "
            f"level={self.level!r}, user_id={self.user_id!r}, "
            f"post_id={self.post_id!r}, message={self.message!r})"
        )
