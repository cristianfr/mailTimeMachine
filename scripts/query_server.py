"""
Script to do a random query in an account.
"""
from timemachine.mail import (
    config_parser,
    connect,
)
from email import message_from_bytes

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Query on an account')
    parser.add_argument('config', help='config file')
    parser.add_argument('account', help='Account to query on.')
    parser.add_argument('query', help='Query to execute')
    parser.add_argument(
        '-results',
        type=int,
        help="Number of results to show",
        default=10)
    args = parser.parse_args()
    accounts = config_parser.load_accounts(args.config)
    account = accounts[args.account]
    mail = connect.ImapConnect(account.server)
    mail.login(account)
    total = mail.count()
    results = mail.run_query(args.query)
    print("Found '{}' results, out of a total of {}".format(len(results), total))
    shown = 0
    while shown < args.results and shown < len(results):
        email = mail.fetch(results[shown])
        shown += 1
        print("=" * 10)
        print("Result No. {}".format(shown))
        print("=" * 10)
        print(message_from_bytes(email))
