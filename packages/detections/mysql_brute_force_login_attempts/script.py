def window():
    return '10m'

def groupby():
    return ['user_host']

def algorithm(event):
    if 'Access denied for user' in event.get('argument', ''):
        return 1.0
    return 0.0

def context(event_data):
    return "Brute force attempt was made on the database which results in {}".format(event_data['argument'])


def criticality():
    return 'Critical'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Brute Force (T1110)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}