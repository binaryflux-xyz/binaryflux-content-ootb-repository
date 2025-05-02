#Add your code here
def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'Accessing Environment' in event['event_Message']:
        if stats.count(event.get("host")) >= 3:
            return 0.50
    return 0.0

def context(event_data):
    return "SwiftUI Environment Access Violations was detected on " + str(event_data['host'])

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Subvert Trust Controls (T1553)'

def artifacts():
    return stats.collect(['host', 'timestamp'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}


