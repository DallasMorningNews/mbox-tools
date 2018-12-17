# Imports from python.  # NOQA
import csv


# Imports from other dependencies.
import mailbox


EXPORT_FIELD_NAMES = [
    'from', 'to', 'cc', 'date', 'subject',
    'body', 'attachments',
    'priority', 'importance', 'sensitivity',
]


def generate_csv_digest(source_file, output_file):
    """Converts a .mbox file to a digest CSV with one row per email.

    These rows include the top-level metadata, along with a field with
    the email message's body text and one with the names of files that
    were sent as attachments.
    """
    all_mail = mailbox.mbox(source_file)
    messages = [_ for _ in all_mail]

    formatted_messages = []

    for message in messages:
        fmt_message = {
            'from': message['From'],
            'to': message['To'],
            'date': message['Date'],
            'subject': message['Subject'],
        }

        if 'cc' in message.keys():
            fmt_message['cc'] = message['cc']
        elif 'Cc' in message.keys():
            fmt_message['cc'] = message['Cc']
        else:
            fmt_message['cc'] = None

        if 'Priority' in message.keys():
            fmt_message['priority'] = message['Priority']
        else:
            fmt_message['priority'] = None

        if 'Importance' in message.keys():
            fmt_message['importance'] = message['Importance']
        else:
            fmt_message['importance'] = None

        if 'Sensitivity' in message.keys():
            fmt_message['sensitivity'] = message['Sensitivity']
        else:
            fmt_message['sensitivity'] = None

        fmt_message['body'] = ' --- MESSAGE PAYLOAD PART BOUNDARY --- '.join([
            item.get_payload() for item in message.get_payload()
            if item.get_content_type() == 'text/plain'
        ]) if message.is_multipart() else message.get_payload().strip()

        fmt_message['attachments'] = '  //  '.join([
            item['Content-Disposition'].split('filename=')[1].strip('"')
            for item in message.get_payload()
            if item.get_content_type() not in [
                'text/plain',
                'message/rfc822',
            ]
        ]) if message.is_multipart() else ''

        formatted_messages.append(fmt_message)

    with open(output_file, 'w') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=EXPORT_FIELD_NAMES)
        writer.writeheader()

        for _ in formatted_messages:
            writer.writerow(_)
