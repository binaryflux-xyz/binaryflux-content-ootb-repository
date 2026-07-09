import re

def transform(event):
    accumulated_domains = set()
    INTERNAL_DOMAIN = "wonderhfl.com"

    email_from_address = event.get('email_from_address', '')
    email_from_domain = email_from_address.split('@')[-1] if '@' in email_from_address else ''
    event['email_from_domain'] = email_from_domain
    accumulated_domains.add(email_from_domain)
    email_fields = ['email_to_address', 'email_reply_to_address', 'email_cc_address', 'email_bcc_address']
    email_body_shortened = ""
    if event.get("email_body") != None
      email_body_shortened = jsoup.extractTextAndLinks(event.get("email_body"))
    event["email_body_shortened"] = email_body_shortened
    
    email_body_links = ""
    if email_body_shortened:
      email_body_links = re.findall(r'https?://[^\s"\'<>]+', email_body_shortened)
        
    email_subject=event.get('email_subject')
    email_subject_links = ""
    if email_subject:
      email_subject_links = re.findall(r'https?://[^\s"\'<>]+', email_subject)
        
    event["email_body_links"] = email_body_links
    event["email_subject_links"]=email_subject_links
  

    # Extract unique domains for each email field
    for field in email_fields:
        domain_key = field + "_domain"
        event[domain_key] = get_unique_domains(event.get(field, []))
        accumulated_domains.update(event[domain_key])  # Accumulate extracted domains

    # Check if email is internal
    event["email_within_company"] = (len(accumulated_domains) == 1 and INTERNAL_DOMAIN in accumulated_domains)

    # Fetch groups for email_from_address
    if event.get("email_folder") == "sent":
        event["email_from_groups"] = graph.getGroup({
            "customer": event.get("customer"),
            "tenant": event.get("tenant"),
            "nodevalue": email_from_address,
            "nodelabel": "group"
        })

        # Initialize recipient_groups before the for loop
        recipient_groups = []

        # Fetch groups for all recipient-related fields
        for field in email_fields:
            email_list = event.get(field, [])

            try:
                for email in email_list:
                    print("Fetching groups for email:", email)
                    groups = graph.getGroup({
                        "customer": event.get("customer"),
                        "tenant": event.get("tenant"),
                        "nodevalue": email,
                        "nodelabel": "group"
                    })
                    print("Groups for", email, ":", groups)
                    if groups:
                        for group in groups:
                            if group not in recipient_groups:
                                recipient_groups.append(group)
            except Exception as e:
                print("Error processing", field, ":", str(e))

        # Ensure recipient_groups is assigned before using it
        if recipient_groups:
            event["email_recipients_groups"] = recipient_groups

    return event

def get_unique_domains(email_list):
    """Extracts unique domains from a list of email addresses."""
    if not email_list:
        return []
    
    return list({email.split('@')[-1] for email in email_list if '@' in email})  # Using set comprehension to avoid duplicates
