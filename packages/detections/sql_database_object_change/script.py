def window():
    return "10m" 

def groupby():
    return ["source_account_name"]

def algorithm(event):
    if event.get('action_id', '').strip() in ['CR', 'AL', 'DR']:
        if stat.count('server_principal_name') > 5:
            return 0.50
    return 0.0


def context(event):
    return 'Database table was altered by ' + str(event.get('server_principal_name', '')) + ' on database ' + str(event.get('database_name', '')) + ' using query ' + str(event.get('statement', ''))

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Persistence (TA0003)'

def technique():
    return 'Event Trigger Execution (T1546)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}