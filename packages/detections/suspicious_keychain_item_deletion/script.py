def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event['event_type'] == 'activityCreateEvent' and "SecItemDelete" in event['event_Message']:
        return 0.9
    return 0.0

def context(event_data):
    return "Deletes sensitive keychain items of " + event_data['host']

def criticality():
    return 'HIGH'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Credentials from Password Stores (T1555)'

def artifacts():
    return stats.collect(['host', 'timestamp'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
