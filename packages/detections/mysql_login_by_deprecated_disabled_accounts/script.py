def window():
    return None

def groupby():
    return None

def algorithm(event):
    user = event.get('user_host', '')
    argument = event.get('argument', '')
    if ('access denied' in argument or
        ('account is locked' in argument or 'password expired' in argument or 'deprecated' in user)):
        return 0.75
    return 0.0



def context(event):
    return "Login attempt by deprecated or disabled account '{}': {}".format(
        event.get('user_host', 'unknown'),
        event.get('argument', '')
    )


def criticality():
    return 'High'

def tactic():
    return 'Persistence (TA0003)'

def technique():
    return 'Valid Accounts (T1078)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}