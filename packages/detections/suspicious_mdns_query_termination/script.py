def window():
    return '10m'

def groupby():
    return ['host']

def algorithm(event):
    if event['event_type'] == 'logEvent' and "mDNS_StopQuery_internal" in event['event_Message']:
        if "mDNS_StopQuery_internal" in event['format_string']:
            return 0.9
    return 0.0

def context(event_data):
    return "An mDNS query was forcefully terminated on " + event_data['host']

def criticality():
    return 'HIGH'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Indicator Removal on Host (T1070)'

def artifacts():
    return stats.collect(['host', 'format_string'])

def entity(event):
    return {'derived': False, 'value': event['host'], 'type': 'device'}
