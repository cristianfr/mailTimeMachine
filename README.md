# mailTimeMachine

Base time machine features for an IMAP mailbox.

Built with the purpose of creating an IMAP mbox backup that can be stored in the cloud, allowing the emails to be deleted from IMAP server and restored locally whenever necessary.

So far it can, which is good enough.

# Usage

Populate the config with the imap accounts, then run:
```python
python scripts/backup.py --help
```

# TODO

Cache the dates of the emails so I don't have to open each email.
