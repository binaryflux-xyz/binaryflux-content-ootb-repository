def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get('action_id', '').strip() in ['CR', 'AL', 'DR'] and event.get('statement', '').startswith('EXEC'):
        return 0.75
    return 0.0

def context(event):
    return 'Server object were modified by executing ' + str(event.get('statement', '')) + ' on database ' + str(event.get('database_name', ''))

def criticality():
    return 'HIGH'

def tactic():
    return 'Lateral Movement (TA0008)'

def technique():
    return 'Remote Services (T1021)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}
