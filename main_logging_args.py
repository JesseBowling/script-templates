#!/usr/bin/env python3
# encoding: utf-8
import logging
import urllib3
import argparse
import configparser
import os.path as path

urllib3.disable_warnings()

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s[%(lineno)s][%(filename)s] - %(message)s'

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def read_config(fn):
    filename = path.expanduser(fn)
    with open(filename) as f:
        c = configparser.RawConfigParser()
        c.read_file(f)
    config = {s: dict(c.items(s)) for s in c.sections()}

    return config

def main():

    parser = argparse.ArgumentParser(
        description='Hit all the places for all the info, write out a CSV file of output (or JSON)',
        epilog='http://xkcd.com/353/')
    parser.add_argument('-d', '--debug', action="store_true", dest='debug',
                        default=False,
                        help='Get debug messages about processing')
    parser.add_argument('--config', dest='conffile',
                        default='~/.conffile',
                        required=False,
                        help='Full path to configuration file to read')
    options = parser.parse_args()

    if options.debug:
        logger.setLevel(logging.DEBUG)

    config = read_config(options.conffile)

if __name__ == '__main__':
    main()
