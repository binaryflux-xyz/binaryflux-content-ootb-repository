def window():
    return "10m" 
  

def groupby():
    return ["server_principal_name"]

def algorithm(event):
    action_id = event.get('action_id', '').strip()
    action_name = event.get('action_name', '').strip()

    if action_id == 'LGIS' and action_name == 'LOGIN SUCCEEDED':
        if stats.count(event.get('server_principal_name')) > 5:
            return 0.25
    elif action_id == 'LGO' and action_name == 'LOGOUT':
        if stats.count(event.get('server_principal_name')) > 5:
            return 0.25
    return 0.0

def context(event):
    action_id = event.get('action_id', '').strip()

    if action_id == 'LGIS':
        return 'Multiple logins were seen for user ' + str(event.get('server_principal_name', '')) + ' in a short duration results in ' + str(event.get('action_name', ''))
    elif action_id == 'LGO':
        return 'Multiple logouts were seen for user ' + str(event.get('server_principal_name', '')) + ' in a short duration results in ' + str(event.get('action_name', ''))


def criticality():
    return 'Low'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Valid Accounts (T1078)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}