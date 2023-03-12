from apps.common.util import InfoException, ErrorCode


class StringManager:

    @staticmethod
    def get_reverse(_string: str) -> str:
        if not _string:
            raise InfoException(ErrorCode.ERROR_CODE_INVALID_STRING)
        return _string[::-1]
