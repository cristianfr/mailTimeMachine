import timemachine.mail.connect as connect
import timemachine.mail.config_parser as config_parser

import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] (%(name)s) - %(threadName)s -  %(levelname)s - %(message)s') 

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.info("Test")
    parser = argparse.ArgumentParser(description="Create backup of IMAP account")
    parser.add_argument('config', help='Location of config')
    parser.add_argument('account_name', help='Account to backup')
    parser.add_argument('output', help='Mailbox to output to.')
    args = parser.parse_args()
    accounts = config_parser.load_accounts(args.config)
    assert accounts.get(args.account_name), (
        "Account not found: Possible {}".format(', '.join(accounts.keys()))
    )
    account = accounts[args.account_name]
    imap = connect.ImapConnect(account.server)
    imap.login(account)
