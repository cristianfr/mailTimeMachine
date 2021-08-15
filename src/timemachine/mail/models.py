"""
Classes to simplify object manipulation.
"""
from email import utils
from datetime import datetime

import pytz
import time


class ImapMessage:

    def __init__(self, payload):
        self.content = payload

    def as_store():
        return self.content[0][1]


class Server:

    def __init__(self, name=None, host=None, port=None):
        self.name = name
        self.host = host
        self.port = port


class Account:

    def __init__(self, name=None, login=None, password=None, server=None):
        self.name = name
        self.login = login
        self.password = password
        self.server = server

class Mbox:

    @staticmethod
    def get_ranges(mbox):
        miny = pytz.utc.localize(datetime.now())
        maxy = datetime(1984, 6, 9, tzinfo=pytz.UTC)
        for message in mbox:
            date = utils.parsedate_to_datetime(message['Date'])
            miny = min(date, miny)
            maxy = max(date, maxy)
        if miny > maxy:
            return None, None
        return miny, maxy 
