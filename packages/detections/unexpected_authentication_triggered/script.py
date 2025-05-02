def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'StatusChangeCallback updated DFR status: 1' in event['event_Message']:
        if stats.count(event.get("host")) > 5:
            return 0.75
    return 0.0

def context(event_data):
    return "DFR status updates detected on " + str(event_data['host'])

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Impair Defenses (T1562)'

def artifacts():
    return stats.collect(['host', 'subsystem'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
