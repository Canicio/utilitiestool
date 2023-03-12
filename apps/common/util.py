
class Constants:

    COMMAND_REVERSE_STRING = '--reverse_string'

    ARG_PATH = '<path>'
    ARG_STRING = '<string>'
    ARG_INTEGER = '<integer>'

    MSG_HELP_COMMAND_REVERSE_STRING = "Get reverse string"

    MODE_OPEN_FILE_W = 'w'
    MODE_OPEN_FILE_R = 'r'
    MODE_OPEN_FILE_R_W = 'r+'

    MSG_EXCEPTION_INVALID_STRING = 'Invalid string'


class ErrorCode:

    ERROR_CODE_INVALID_STRING = 700

    @staticmethod
    def manage_info_exception(e):
        if ErrorCode.ERROR_CODE_INVALID_STRING in e.args:
            print(Constants.MSG_EXCEPTION_INVALID_STRING)


class InfoException(Exception):
    pass
