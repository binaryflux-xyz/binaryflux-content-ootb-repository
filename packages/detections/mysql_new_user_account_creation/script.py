def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '').upper()
    if 'CREATE USER' in argument:
        return 0.75
    return 0.0


def context(event):
    return "New user account created: {} by {}".format(
        event.get('argument', ''),
        event.get('user_host', 'unknown')
    )

def criticality():
    return 'High'

def tactic():
    return 'Persistence (TA0003)'

def technique():
    return 'Create Account (T1136)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}