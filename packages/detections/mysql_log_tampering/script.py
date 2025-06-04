def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '').upper()
    if any(keyword in argument for keyword in ['SET GLOBAL', 'TRUNCATE TABLE', 'DELETE FROM']):
        return 1.0  # High severity
    return 0.0

def context(event_data):
    argument = event_data.get('argument', '')
    user = event_data.get('user_host', 'unknown user')
    return '"{}" was performed on the table by {}'.format(argument, user)


def criticality():
    return 'Critical'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Indicator Removal on Host (T1070)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}