def window():
    return "10m" 
  

def groupby():
    return ["server_principal_name"]

def algorithm(event):
    object_name = event.get('event_type', '').strip()
    action_name = event.get('action_name', '').strip()

    if object_name == 'sysjobs' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.50
    elif object_name == 'sysjobs_view' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.50
    elif object_name == 'Users' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.50
    elif object_name == 'Event' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.50
    return 0.0

def context(event):
    object_name = event.get('event_type', '').strip()
    user = str(event.get('server_principal_name', 'Unknown'))
    statement = str(event.get('statement', 'a SQL operation'))

    if object_name == 'sysjobs':
        return "User '" + user + "' queried SQL Server Agent jobs (sysjobs) with the statement: " + statement + " - potential lateral movement activity."
    elif object_name == 'sysjobs_view':
        return "User '" + user + "' viewed SQL Server Agent job details (sysjobs_view) with the statement: " + statement + " - may indicate intent to persist via jobs."
    elif object_name == 'Users':
        return "User '" + user + "' accessed internal user mapping (Users) with the statement: " + statement + " - may be mapping logins to database users."
    elif object_name == 'Event':
        return "User '" + user + "' accessed internal event logs (Event) with the statement: " + statement + " - possible audit evasion or reconnaissance."


def criticality():
    return 'Medium'

def tactic():
    return 'Discovery (TA0007)'

def technique():
    return 'Account Discovery (T1087)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}