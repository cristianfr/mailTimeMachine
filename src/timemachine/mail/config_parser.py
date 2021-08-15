"""
Anything related to translating the configs to the models. Including
validations.
"""
import timemachine.mail.models as models

import yaml


def validate_config(config):
    assert 'servers' in config
    assert 'accounts' in config
    for server, account in config['accounts'].items():
        assert server in config['servers']


def load_accounts(filename):
    with open(filename, 'r') as infile:
        config = yaml.load(infile, Loader=yaml.Loader)
    validate_config(config)
    all_servers = {}
    all_accounts = {}
    for name in config['servers']:
        all_servers[name] = models.Server(name=name, **config['servers'][name])
    for server in config['accounts']:
        for account in config['accounts'][server]:
            all_accounts[account] = models.Account(
                name=account,
                server=all_servers[server],
                **config['accounts'][server][account])
    return all_accounts
