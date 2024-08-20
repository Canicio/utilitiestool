from apps.common.util import InfoException, ErrorCode
import base64

# import base64
# b = base64.b64encode(bytes('your_string', 'utf-8')) # bytes
# base64_str = b.decode('utf-8') # convert bytes to string


class ObfuscationManager:

    @staticmethod
    def get_base64_encoding(_string: str) -> str:
        if not _string:
            raise InfoException(ErrorCode.ERROR_CODE_INVALID_STRING)
        return base64.b64encode(bytes(_string, 'utf-8')).decode('utf-8')

    @staticmethod
    def get_base64_decoding(_string: str) -> str:
        if not _string:
            raise InfoException(ErrorCode.ERROR_CODE_INVALID_STRING)
        return base64.b64decode(bytes(_string, 'utf-8')).decode('utf-8')
