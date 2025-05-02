def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event['event_type'] == 'logEvent' and 'incorrect password' in event['event_Message'].lower():
        if stats.count('host') > 2:
            return 0.8
    return 0.0

def context(event_data):
    return "Multiple sudo authentication failures detected on " + event_data['host']

def criticality():
    return 'HIGH'

def tactic():
    return 'Privilege Escalation (TA0004)'

def technique():
    return 'Sudo and Sudoers (T1548.003)'

def artifacts():
    return stats.collect(['host', 'event_Message'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
