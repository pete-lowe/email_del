from imapclient import IMAPClient

server = IMAPClient('imap.gmail.com')
server.login('example@gmail.com', 'example')
server.select_folder('Inbox')
messages_to_del = server.search(('UNSEEN'))
unread_mail_count = len(messages_to_del)
server.delete_messages(messages_to_del)
print(f'You have deleted {unread_mail_count} messages from your mailbox.')
