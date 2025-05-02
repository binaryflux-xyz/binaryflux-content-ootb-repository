#Add your code here
def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'Users on removed smartcard' in event['event_Message']:
        if stats.count(event.get("host")) >= 5:
            return 0.25
    return 0.0

def context(event_data):
    return "Multiple Smartcard Removal Events Detected" + str(event_data['host'])

def criticality():
    return 'Low'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Modify Authentication Process (T1556)'

def artifacts():
    return stats.collect(['host', 'timestamp'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
