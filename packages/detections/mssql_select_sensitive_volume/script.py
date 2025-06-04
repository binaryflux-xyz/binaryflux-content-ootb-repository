def window():
    return '5m'
def groupby():
    return 'user_name'
def algorithm(event):
    if event['action'] == 'SELECT' and event['object_name'] in tpi.sensitive_tables():
        if stats.count('object_name') >= 20:
            return 0.9
    return 0.0
def context(event_data):
    return (
        "Unusual volume of SELECT queries detected on sensitive table(s) by account "
        + event_data['user_name'] + " from IP " + event_data['source_ip'] + "."
    )
def criticality():
    return 'CRITICAL'
def tactic():
    return 'Exfiltration (TA0010)'
def technique():
    return 'Exfiltration Over Application Layer (T1048.003)'
def artifacts():
    return stats.collect(['user_name', 'source_ip',  'process_command_line'])
def entity(event):
    return {'derived': False, 'value': event['user_name'], 'type': 'user'}