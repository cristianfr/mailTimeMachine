"""
Connection shennanigans
"""
import imaplib
import logging

logger = logging.getLogger(__name__)


class ImapConnect:

    date_format = '%d-%b-%Y'
    body_format = "(RFC822)"

    def __init__(self, server):
        logger.info("Connecting to server... %s", server.host)
        self.mail = imaplib.IMAP4_SSL(server.host)
        logger.info("Connected!")

    def login(self, account):
        logger.info("Authenticating... %s", account.login)
        self.mail.login(account.login, account.password)
        logger.info("Done")

    def count(self):
        status, cnt = self.mail.select()
        return int(cnt[0])

    def run_query(self, query):
        result, data = self.mail.search(None, '({})'.format(query))
        return data[0].split()

    def fetch(self, idx):
        status, data = self.mail.fetch(idx, self.body_format)
        return data[0][1]

    def get_ids_between(self, sent_before, sent_since):
        """
        Select emails within a certain timezone independent time range.
        Returns ids between those dates.
        """
        assert sent_since < sent_before
        query = 'SENTBEFORE "{}" SENTSINCE "{}"'.format(
            sent_before.strftime(self.date_format),
            sent_since.strftime(self.date_format)
        )
        logger.debug(query)
        return self.run_query(query)

    def store_ids(self, id_list, mbox):
        """
        Fetch the message of the ids.
        """
        mbox.lock()
        try:
            for cnt, idx in enumerate(id_list):
                mbox.add(self.fetch(idx))
        finally:
            logger.info("Wrote to %s to mbox", cnt + 1)
            mbox.flush()
            mbox.unlock()

    def store_ids_between(self, sent_before, sent_since, mbox, batch_size=10):
        """
        Store emails with batch size.
        """
        ids = self.get_ids_between(sent_before, sent_since)
        logger.info(
            "Found %s emails between %s and %s",
            len(ids), sent_since, sent_before)
        first = 0
        batches_processed = 0
        total_batches = len(ids)/batch_size + 1
        while first < len(ids):
            self.store_ids(ids[first:first + batch_size], mbox)
            first = first + batch_size
            batches_processed += 1
            logger.info("{:.2f}% Done".format(
                batches_processed * 100.0 /total_batches))
        mbox.close()
        logger.info("Done!")
