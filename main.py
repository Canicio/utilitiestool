import argparse
from apps.common.util import Constants, InfoException, ErrorCode
from apps.obfuscation.manager import ObfuscationManager
from apps.strings.manager import StringManager


class App(object):
    """App class containing the main method"""

    @staticmethod
    def main() -> None:
        """Main method"""

        try:

            # Get input arguments
            parser = argparse.ArgumentParser()
            parser.add_argument(Constants.COMMAND_REVERSE_STRING, metavar=Constants.ARG_STRING,
                                nargs=1, type=str, help=Constants.MSG_HELP_COMMAND_REVERSE_STRING)
            parser.add_argument(Constants.COMMAND_ENCODE_BASE64, metavar=Constants.ARG_STRING,
                                nargs=1, type=str, help=Constants.MSG_HELP_COMMAND_ENCODE_BASE64)
            parser.add_argument(Constants.COMMAND_DECODE_BASE64, metavar=Constants.ARG_STRING,
                                nargs=1, type=str, help=Constants.MSG_HELP_COMMAND_DECODE_BASE6)
            args = parser.parse_args()

            # Business logic calls
            if args.reverse_string:
                result = StringManager.get_reverse(_string=args.reverse_string[0])
                print(result)
            if args.encode_base64:
                result = ObfuscationManager.get_base64_encoding(_string=args.encode_base64[0])
                print(result)
            if args.decode_base64:
                result = ObfuscationManager.get_base64_decoding(_string=args.decode_base64[0])
                print(result)
        except InfoException as e:
            ErrorCode.manage_info_exception(e)


if __name__ == '__main__':
    App.main()
