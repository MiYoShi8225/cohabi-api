import json
from typing import List


class ApiError:
    def __init__(self, error_code: str = "", error_messages: List[str] = []) -> None:
        self.error_code = error_code
        self.error_messages = error_messages


class ApiResult:
    def __init__(self, result: ApiError = ApiError(error_code="", error_messages=[]), body: dict = None):
        self.result = {
            'error_code': result.error_code,
            'error_messages': result.error_messages
        }
        self.body = body

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)
