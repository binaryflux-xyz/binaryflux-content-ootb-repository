def condition(event):
    event_type = event.get('event_type')
    event_id = event.get('event_id')
    
    audit_failure_ids = {"4957", "4673", "4625","4953", "5152", "5157", "4768", "4674", "4769", "4771", "4776"}
    
    return event_type == 'AUDIT_FAILURE' and event_id in audit_failure_ids
