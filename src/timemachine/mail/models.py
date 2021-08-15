"""
Classes to simplify object manipulation.
"""
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
