
#Add your code here
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if not event.get('statement'):
        return 0.0

    if event.get('action_id', '').strip() in ['EX', 'APRL', 'DPRL']:
        return 0.75

    return 0.0


def context(event):
    return 'Database Role Changes were made using the statement ' + str(event.get('statement', '')) + ' by user ' + str(event.get('server_principal_name', '')) + ' on database ' + str(event.get('database_name', ''))

def criticality():
    return 'HIGH'

def tactic():
    return 'Privilege Escalation (TA0004)'

def technique():
    return 'Valid Accounts (T1071)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}