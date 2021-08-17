from timemachine.mail import config_parser

import pytest
import os


@pytest.mark.parametrize(
    "config,account",
    [("config.yml", "cristian"), ("config.yml", "natally")]
)
def test_config_parser(resources, config, account): 
    accounts = config_parser.load_accounts(os.path.join(resources, config))
    assert account in accounts


@pytest.mark.parametrize(
    "config,account",
    [("invalid.yml", "cristian")]
)
def test_invalid_configs(resources, config, account):
    with pytest.raises(Exception):
        accounts = config_parser.load_accounts(os.path.join(resources, config))
