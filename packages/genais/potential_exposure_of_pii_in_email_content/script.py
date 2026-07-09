

def skip(event):
  if event.get("email_folder") == "sent":
    return False  # Modify logic if skipping conditions exist
  else:
    return True


def content(event):
    """
    Extracts and formats email content from the event (Python 2 compatible).
    """
    email_text = htmltotext.format(event.get("email_body", ""))

    content = (
        "from : {}\n"
        "to : {}\n"
        "cc : {}\n"
        "bcc : {}\n\n"
        "subject : {}\n\n"
        "body :\n\n\n{}\n\n\n"
        "attachments : {}".format(
            event.get("email_header_from", ""),
            ", ".join(event.get("email_to_address", [])),
            ", ".join(event.get("email_cc_address", [])) or "-",
            ", ".join(event.get("email_bcc_address", [])) or "-",
            event.get("email_subject", ""),
            email_text.strip(),
            ", ".join(event.get("email_attachments_name", []))
        )
    )

    return content


def agent():
    """
    Returns the predefined agent type.
    """
    return "email-pii"