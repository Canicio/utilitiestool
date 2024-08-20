
class Constants:

    COMMAND_REVERSE_STRING = '--reverse_string'
    COMMAND_ENCODE_BASE64 = '--encode_base64'
    COMMAND_DECODE_BASE64 = '--decode_base64'

    ARG_PATH = '<path>'
    ARG_STRING = '<string>'
    ARG_STRING_WITH_QUOTES = '"<string>"'
    ARG_INTEGER = '<integer>'

    MSG_HELP_COMMAND_REVERSE_STRING = "Get reverse string (use quotes if there are spaces)"
    MSG_HELP_COMMAND_ENCODE_BASE64 = "Get Base64 encoding (use quotes if there are spaces)"
    MSG_HELP_COMMAND_DECODE_BASE6 = "Get Base64 decoding"

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
