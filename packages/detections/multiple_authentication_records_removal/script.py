def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get('event_type') == 'logEvent' and 'removing auth record' in event.get('event_Message', ''):
        return 0.8
    return 0.0

def context(event_data):
    return "Potential unauthorized removal of authentication records detected on " + str(event_data['host'])

def criticality():
    return 'HIGH'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Indicator Removal on Host (T1070)'

def artifacts():
    return stats.collect(['host', 'subsystem'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
