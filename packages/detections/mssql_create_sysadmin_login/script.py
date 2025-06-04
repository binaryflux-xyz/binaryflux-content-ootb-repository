def window():
    return '5m'
def groupby():
    return 'user_name'
def algorithm(event):
    if "CREATE LOGIN" in event['process_command_line'].upper() and "sysadmin" in event['process_command_line'].lower():
        return 1.0
    return 0.0
def context(event_data):
    return (
        "New SQL login with elevated privileges created by " +
        event_data['user_name'] + ": " + event_data['process_command_line']
    )
def criticality():
    return 'HIGH'
def tactic():
    return 'Persistence (TA0003)'
def technique():
    return 'Create Account (T1136)'
def artifacts():
    return stats.collect(['user_name', 'process_command_line', 'source_ip'])
def entity(event):
    return {'derived': False, 'value': event['user_name'], 'type': 'user'}
