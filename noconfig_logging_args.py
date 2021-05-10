#!/usr/bin/env python3
# encoding: utf-8
import logging
import urllib3
import argparse
import os

urllib3.disable_warnings()

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s[%(lineno)s][%(filename)s] - %(message)s'

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def options_from_env(keys=[]):
    options = {}
    for k in keys:
        v = os.getenv(k, None)
        options[k] = v

    return options

def main():

    parser = argparse.ArgumentParser(
        description='Template Description',
        epilog='http://xkcd.com/353/')
    parser.add_argument('-d', '--debug', action="store_true", dest='debug',
                        default=False,
                        help='Get debug messages about processing')

    options = parser.parse_args()
    env_opts = options_from_env(['DEBUG'])

    if options.debug:
        logger.setLevel(logging.DEBUG)
    elif env_opts['DEBUG'] and env_opts['DEBUG'].lower() == 'true':
        logger.setLevel(logging.DEBUG)

    logger.debug('Debug logging enabled!')
    logger.debug(f'Retrieved from CLI: {options.__dict__}')
    logger.debug(f'Retrieved from env: {env_opts}')

if __name__ == '__main__':
    main()
