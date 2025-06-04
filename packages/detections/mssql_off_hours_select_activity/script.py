def window():
    return '10m'
def groupby():
    return 'user_name'
def algorithm(event):
    hour = int(event['timestamp'].split('T')[1].split(':')[0])
    if hour < 6 or hour > 22:
        if event['action'] == 'SELECT':
            if stats.count('statement') > 30:
                return 0.85
    return 0.0
def context(event_data):
    return (
        "High volume of SELECT queries detected outside normal hours by user "
        + event_data['user_name'] + " from IP " + event_data['source_ip'] + "."
    )
def criticality():
    return 'MEDIUM'
def tactic():
    return 'Exfiltration (TA0010)'
def technique():
    return 'Data Transfer Size Anomaly (Custom Heuristic)'
def artifacts():
    return stats.collect(['user_name', 'statement', 'timestamp', 'source_ip'])
def entity(event):
    return {'derived': False, 'value': event['user_name'], 'type': 'user'}