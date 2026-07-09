def window():
    return '30m'
def groupby():
    return ['user_name']
def algorithm(event):
    if event['event_id'] == 20225 and event['location'] not in ['US', 'UK', 'CA']:
        return 0.9
    return None
def context(event_data):
    return "VPN connection from an unusual location: " + event_data['location']
def criticality():
    return 'HIGH'
def tactic():
    return 'Defense Evasion (TA0005)'
def technique():
    return 'Network Connection via VPN (T1572)'
def artifacts():
    return stats.collect(['user_name', 'location', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['user_name'], 'type': 'user'}