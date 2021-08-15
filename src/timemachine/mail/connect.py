"""
Connection shennanigans
"""
import imaplib
import logging

logger = logging.getLogger(__name__)


class ImapConnect:

    def __init__(self, server):
        logger.info("Connecting to server... %s", server.host)
        self.mail = imaplib.IMAP4_SSL(server.host)
        logger.info("Connected!")

    def login(self, account):
        logger.info("Authenticating... %s", account.login)
        self.mail.login(account.login, account.password)
        logger.info("Done")
