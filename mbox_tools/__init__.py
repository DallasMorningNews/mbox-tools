# Imports from python.  # NOQA
import csv


# Imports from other dependencies.
import mailbox


EXPORT_FIELD_NAMES = [
    'from', 'to', 'cc', 'date', 'subject',
    'body', 'attachments',
    'priority', 'importance', 'sensitivity', 'msg_size'
]


def generate_csv_digest(source_file, output_file):
    """Converts a .mbox file to a digest CSV with one row per email.

    These rows include the top-level metadata, along with a field with
    the email message's body text and one with the names of files that
    were sent as attachments.
    """
    all_mail = mailbox.mbox(source_file)

    formatted_messages = []

    for message in all_mail:
        fmt_message = {
            'from': message['From'],
            'to': message['To'],
            'date': message['Date'],
            'subject': message['Subject'],
        }

        if 'cc' in message.keys():
            fmt_message['cc'] = message.get('cc')
        else:
            fmt_message['cc'] = message.get('Cc')

        fmt_message['priority'] = message.get('Priority')
        fmt_message['importance'] = message.get('Importance')
        fmt_message['sensitivity'] = message.get('Sensitivity')
        try:
            fmt_message['msg_size'] = len(message.as_string())
        except KeyError:
            fmt_message['msg_size'] = 0

        fmt_message['body'] = ' --- MESSAGE PAYLOAD PART BOUNDARY --- '.join([
            item.get_payload() for item in message.get_payload()
            if item.get_content_type() == 'text/plain'
        ]) if message.is_multipart() else message.get_payload().strip()

        fmt_message['attachments'] = ''
        if message.is_multipart():
            filenames = [x.get_filename() for x in message.get_payload() if x.get_filename()]
            if filenames:
                fmt_message['attachments'] = '  //  '.join(filenames)

        formatted_messages.append(fmt_message)

    with open(output_file, 'w') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=EXPORT_FIELD_NAMES)
        writer.writeheader()

        for _ in formatted_messages:
            writer.writerow(_)
