def window():
    return None
def groupby():
    return None
def algorithm(event):
    if event['event_id'] == 5145 and event['share_name'] in ['C$', 'ADMIN$']:
        return 0.85
    return None
def context(event_data):
    return "Unauthorized access attempt to SMB share " + event_data['share_name']
def criticality():
    return 'HIGH'
def tactic():
    return 'Lateral Movement (TA0008)'
def technique():
    return 'Remote Services: SMB (T1021.002)'
def artifacts():
    return stats.collect(['share_name', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['share_name'], 'type': 'service'}