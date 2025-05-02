def window():
    return None
def groupby():
    return None
def algorithm(event):
    if event['event_id'] == 4657 and 'Run' in event['registry_path']:
        return 0.85
    return None
def context(event_data):
    return "Suspicious registry modification detected in " + event_data['registry_path']
def criticality():
    return 'HIGH'
def tactic():
    return 'Persistence (TA0003)'
def technique():
    return 'Registry Run Keys / Startup Folder (T1547.001)'
def artifacts():
    return stats.collect(['registry_path', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['registry_path'], 'type': 'registry'}