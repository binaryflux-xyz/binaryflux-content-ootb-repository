#Add your code here
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'updateLocalNetworkConfigurations' in event.get('event_Message', ''):
        return 0.25
    return 0.0

def context(event_data):
    return "Configuration for Local Network Access detected on " + str(event_data['host'])

def criticality():
    return 'Low'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Modify Authentication Process (T1556)'

def artifacts():
    return stats.collect(['host', 'subsystem'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}

