def window():
    return '10m'

def groupby():
    return 'thread_id'

def algorithm(event):
    if event['event_type'] == 'logEvent' and 'service account' in event['format_string'].lower():
        return 0.85
    return 0.0

def context(event_data):
    return "Access attempt detected using a shared/service account. Thread ID: " + str(event_data['thread_id'])

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Valid Accounts (T1078)'

def artifacts():
    return stats.collect(['thread_id', 'event_type', 'format_string'])

def entity(event):
    return {'derived': False, 'value': event['thread_id'], 'type': 'thread'}
