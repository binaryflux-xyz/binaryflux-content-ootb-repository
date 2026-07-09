def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '').upper()
    keywords = ['GRANT ALL', 'CREATE USER', 'ALTER USER', 'UPDATE MYSQL.USER']
    if any(k in argument for k in keywords):
        return 1.0
    return 0.0

def context(event):
    return '"{}" attempted by {}'.format(event.get('argument', ''), event.get('user_host', 'unknown'))


def criticality():
    return 'Critical'

def tactic():
    return 'Privilege Escalation (TA0004)'

def technique():
    return 'Abuse Elevation Control Mechanism (T1548)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}