def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event['event_type'] == 'logEvent' and "turning firewall off" in event['event_Message'].lower():
        if "firewall off" in event['format_string']:
            return 0.9
    return 0.0

def context(event_data):
    return "Firewall was disabled on " + event_data['host']

def criticality():
    return 'HIGH'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Impair Defenses (T1562)'

def artifacts():
    return stats.collect(['host', 'format_string'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
