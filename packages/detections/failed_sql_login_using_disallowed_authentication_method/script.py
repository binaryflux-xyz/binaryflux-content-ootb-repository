#Add your code here
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get('action_name') == 'LOGIN FAILED' and 'Login failed for user' in event.get('statement', ''):
        return 0.50
    return 0.0

def context(event_data):
    return (event_data['statement'])

def criticality():
    return 'Medium'

def tactic():
    return 'Credential Access (TA0006)'

def technique():
    return 'Valid Accounts (T1078)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}