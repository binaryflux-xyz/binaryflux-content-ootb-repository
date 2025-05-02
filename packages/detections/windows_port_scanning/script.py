def window():
    return '2m'
def groupby():
    return ['source_ip']
def algorithm(event):
    if event['event_id'] in [5152, 5157] and stats.count('destination_port') > 20:
        return 0.85
    return None
def context(event_data):
    return "Possible port scanning activity detected from " + event_data['source_ip']
def criticality():
    return 'MEDIUM'
def tactic():
    return 'Reconnaissance (TA0043)'
def technique():
    return 'Network Service Scanning (T1046)'
def artifacts():
    return stats.collect(['source_ip', 'destination_port', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['source_ip'], 'type': 'ip'}