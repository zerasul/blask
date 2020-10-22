import argparse
import logging
from blask import BlaskApp

application=BlaskApp().app

if __name__ == '__main__':
    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--debug", action='store_true', help="Verbose output")
    parser.add_argument(
        "-v", "--verbose", action='store_true', help="Verbose output")
    args = parser.parse_args()
    if args.debug or args.verbose:
        log = logging.getLogger()
        level = logging.getLevelName(logging.DEBUG)
        log.setLevel(level)
        debug = True
    else:
        debug = False
    application.run(debug=debug)
