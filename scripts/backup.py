from timemachine.mail import (
    config_parser,
    connect,
    models,
)

from datetime import datetime

import argparse
import mailbox
import logging
import pytz
import sys

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] (%(name)s) - %(levelname)s - %(message)s')


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description="Create backup of IMAP account")
    parser.add_argument('config', help='Location of config')
    parser.add_argument('account_name', help='Account to backup')
    parser.add_argument('--since', help='Since date', default='2021-08-11')
    parser.add_argument('--before', help='Before date', default='2021-08-25')
    parser.add_argument('--batch', type=int, help='Batch size', default=10)
    parser.add_argument('--output', help='Mailbox to output to.')
    parser.add_argument('-log', help="Log file")
    args = parser.parse_args()

    if args.log:
    	handler = logging.FileHandler(args.log)
    	handler.setLevel(logging.INFO)
    	logger.addHandler(handler)

    mbox_file = args.output or '{}.mbox'.format(args.account_name.split('@')[0])
    accounts = config_parser.load_accounts(args.config)
    assert accounts.get(args.account_name), (
        "Account not found: Possible {}".format(', '.join(accounts.keys()))
    )
    sent_before = pytz.utc.localize(datetime.strptime(args.before, '%Y-%m-%d'))
    sent_since = pytz.utc.localize(datetime.strptime(args.since, '%Y-%m-%d'))
    account = accounts[args.account_name]

    logger.info("Loading existing mail box file.")
    mbox = mailbox.mbox(mbox_file)
    logger.info("Found {} messages in file".format(len(mbox)))
    first, last = models.Mbox.get_ranges(mbox)
    logger.info("Mailbox currently contains between %s and %s", first, last)
    if first and last and last > sent_since > first:
        logger.info(
            "Latest email (%s) in mbox is after sent_since (%s), setting "
            "sent_since to last (%s)",
            last, sent_since, last)
        sent_since = last
    if first and last and first < sent_before < last:
        logger.info(
            "First email in mbox (%s) is before sent_before (%s). Setting "
            "sent_before to first (%s)", first, sent_before, first)
        sent_before = first
    if sent_before == first and sent_since == last:
        logger.info("No new emails to find.")
        sys.exit(0)

    # Download from server.
    imap = connect.ImapConnect(account.server)
    imap.login(account)
    cnt = imap.count()
    logger.info("Found %s emails", cnt)
    imap.store_ids_between(sent_before, sent_since, mbox, args.batch)
