def window():
    return "10m" 
  

def groupby():
    return ["server_principal_name"]

def algorithm(event):
    object_name = event.get('event_type', '').strip()
    action_name = event.get('action_name', '').strip()

    if object_name == 'server_role_members' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.75
    elif object_name == 'server_principals' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.75
    elif object_name == 'SecData' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.75
    elif object_name == 'sysjobactivity' and action_name == 'SELECT':
        if stats.count(event.get('event_type')) > 5:
            return 0.75
    return 0.0

def context(event):
    object_name = event.get('event_type', '').strip()
    user = str(event.get('server_principal_name', 'Unknown'))
    statement = str(event.get('statement', 'a SQL operation'))

    if object_name == 'server_role_members':
        return "User '" + user + "' queried role memberships with the statement: " + statement + " - potential lateral movement activity."
    elif object_name == 'server_principals':
        return "User '" + user + "' accessed server-level principals with the statement: " + statement + " - may be mapping users for privilege escalation."
    elif object_name == 'SecData':
        return "User '" + user + "' accessed security descriptor data with the statement: " + statement + " - potential ACL abuse."
    elif object_name == 'sysjobactivity':
        return "User '" + user + "' modified SQL Agent job activity metadata with the statement: " + statement + " - possible attempt to manipulate job execution records."




def criticality():
    return 'High'

def tactic():
    return 'Discovery (TA0007)'

def technique():
    return 'Account Discovery (T1087)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}