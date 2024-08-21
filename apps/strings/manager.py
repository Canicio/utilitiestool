from apps.common.util import InfoException, ErrorCode
import random
import string


class StringManager:

    @staticmethod
    def get_reverse(_string: str) -> str:
        StringValidator.check_string(_string)
        return _string[::-1]

    @staticmethod
    def inject_random_alphanumeric_character(_string: str, position: int) -> str:
        StringValidator.check_string(_string)
        StringValidator.check_position_of_string(_string, position, include_last_extra_position=True)
        random_alphanumeric_char = ''.join(random.choices(string.ascii_letters + string.digits, k=1))
        return '%s%s%s' % (_string[:position], random_alphanumeric_char, _string[position:])

    @staticmethod
    def remove_character(_string: str, position: int) -> str:
        StringValidator.check_string(_string)
        StringValidator.check_position_of_string(_string, position)
        return '%s%s' % (_string[:position], _string[position+1:])


class StringValidator:

    @staticmethod
    def check_string(_string: str):
        if not _string:
            raise InfoException(ErrorCode.ERROR_CODE_INVALID_STRING)

    @staticmethod
    def check_position_of_string(_string: str, position: int, include_last_extra_position=False):
        if include_last_extra_position:
            max_position = len(_string)
        else:
            max_position = len(_string)-1
        if position > max_position or position < 0:
            raise InfoException(ErrorCode.ERROR_CODE_INVALID_POSITION)