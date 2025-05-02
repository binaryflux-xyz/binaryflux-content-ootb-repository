def window():
    return '10m'
def groupby():
    return ['query_name']
def algorithm(event):
    if event['event_id'] == 22 and stats.count('query_name') > 50:
        return 0.9
    return None
def context(event_data):
    return "High volume of DNS requests detected for " + event_data['query_name']
def criticality():
    return 'HIGH'
def tactic():
    return 'Command and Control (TA0011)'
def technique():
    return 'DNS Tunneling (T1071.004)'
def artifacts():
    return stats.collect(['query_name', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['query_name'], 'type': 'dns'}