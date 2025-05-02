def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'configopen() failed: 1100: Permission denied' in event['event_Message']:
        if stats.count(event.get("host")) > 3:
            return 0.50
    return 0.0

def context(event_data):
    return "Repeated Unauthorized Access to System Configuration " + str(event_data['host'])

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Abuse Elevation Control Mechanism (T1548)'

def artifacts():
    return stats.collect(['host', 'timestamp'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
