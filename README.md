# mailTimeMachine

Time machine features for an IMAP mailbox.

Built with the purpose of creating an IMAP mbox backup that can be stored in the cloud, allowing the emails to be deleted from IMAP server.

# Usage

Populate the config with the imap accounts, then run:

python timemachine.mail.main --since yyyy-mm-dd --before yyyy-mm-dd --output <mbox file> config account


# TODO

Cache the dates of the emails so I don't have to open each email.