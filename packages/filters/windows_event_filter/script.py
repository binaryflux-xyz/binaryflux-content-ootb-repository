def condition(event):
    if event.get('event_id') in ['4688', '4648', '5140', '5145', '4624', '4673', '528', '540', '1102', '517']:
        return True
    return False
