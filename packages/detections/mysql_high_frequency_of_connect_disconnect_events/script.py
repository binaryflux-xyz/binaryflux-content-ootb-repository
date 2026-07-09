def window():
    return '10m'

def groupby():
    return ['user_host']

def algorithm(event, stats):
    if event.get('command_type') == 'Connect':
        if stats.get(event.get('user_host'), 0) > 10:
            return 0.50
    return 0.0

def context(event_data):
    return "High frequency of MySQL connections detected from {}".format(event_data.get('user_host', 'unknown'))


def criticality():
    return 'Medium'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Brute Force (T1110)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}