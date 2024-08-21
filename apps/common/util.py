
class Constants:

    COMMAND_REVERSE_STRING = '--reverse_string'
    COMMAND_ENCODE_BASE64 = '--encode_base64'
    COMMAND_DECODE_BASE64 = '--decode_base64'
    COMMAND_INJECT_RANDOM_ALPHANUMERIC_CHAR_IN_STRING = '--inject_random_alphanum_char'
    COMMAND_REMOVE_CHARACTER = '--remove_char'

    ARG_PATH = '<path>'
    ARG_STRING = '<string>'
    ARG_STRING_WITH_QUOTES = '"<string>"'
    ARG_INTEGER = '<integer>'

    MSG_HELP_COMMAND_REVERSE_STRING = "Get reverse string (use quotes if there are spaces)"
    MSG_HELP_COMMAND_ENCODE_BASE64 = "Get Base64 encoding (use quotes if there are spaces)"
    MSG_HELP_COMMAND_DECODE_BASE6 = "Get Base64 decoding (use quotes if there are spaces)"
    MSG_HELP_COMMAND_INJECT_RANDOM_ALPHANUMERIC_CHAR_IN_STRING = ("Inject random alphanumeric character at position "
                                                                  "(integer) in string. For example:\n  $ utilitiestool"
                                                                  " --inject_random_alphanum_char 3 abcdef\nOUTPUT: "
                                                                  "abcXdef")
    MSG_HELP_COMMAND_REMOVE_CHARACTER = ("Remove character at position (integer) in string. For example:\n  $ "
                                         "utilitiestool --remove_char 3 abcdef\nOUTPUT: abcef")

    MODE_OPEN_FILE_W = 'w'
    MODE_OPEN_FILE_R = 'r'
    MODE_OPEN_FILE_R_W = 'r+'

    MSG_EXCEPTION_INVALID_STRING = 'Invalid string'
    MSG_EXCEPTION_INVALID_POSITION = 'Invalid position'


class ErrorCode:

    ERROR_CODE_INVALID_STRING = 700
    ERROR_CODE_INVALID_POSITION = 701

    @staticmethod
    def manage_info_exception(e):
        if ErrorCode.ERROR_CODE_INVALID_STRING in e.args:
            print(Constants.MSG_EXCEPTION_INVALID_STRING)
        elif ErrorCode.ERROR_CODE_INVALID_POSITION in e.args:
            print(Constants.MSG_EXCEPTION_INVALID_POSITION)


class InfoException(Exception):
    pass
