def condition(event):
    audit_failure_event_ids = {"4957", "4673", "4625", "4953", "5152", "5157", "4768", "4674", "4769", "4771", "4776"}
    if event.get('event_type') == 'AUDIT_FAILURE' and event.get('event_id') not in audit_failure_event_ids:
        return True
    else:
        return False