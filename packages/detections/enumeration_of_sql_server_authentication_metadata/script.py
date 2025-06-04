def window():
    return "10m" 
  

def groupby():
    return ["server_principal_name"]

def algorithm(event):
    object_name = event.get('event_type', '').strip()
    action_name = event.get('action_name', '').strip()

    if object_name == 'syslogins' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 1.0
    elif object_name == 'syscachedcredentials' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 1.0
    return 0.0

def context(event):
    object_name = event.get('event_type', '').strip()
    user = str(event.get('server_principal_name', 'Unknown'))
    statement = str(event.get('statement', 'a SQL operation'))

    if object_name == 'syslogins':
        return "User '" + user + "' accessed login metadata (syslogins) with the statement: " + statement + " - may indicate credential reconnaissance."
    elif object_name == 'syscachedcredentials':
        return "User '" + user + "' accessed cached credentials (syscachedcredentials) with the statement: " + statement + " - high risk of credential compromise."


def criticality():
    return 'Critical'

def tactic():
    return 'Discovery (TA0007)'

def technique():
    return 'Account Discovery (T1087)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}