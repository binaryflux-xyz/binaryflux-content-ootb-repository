"""
Instructions for Content Creators:
- Implement the required functions based on your detection algorithm and use case.
- Each function has a placeholder for customization.
"""

#Add your code here
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get('action_id', '').strip() == 'IMP':
        return 0.75
    return 0.0

def context(event):
    return 'Server Changes were made by executing query ' + str(event.get('statement', '')) + ' by user ' + str(event.get('server_principal_name', '')) + ' on database ' + str(event.get('database_name', ''))

def criticality():
    return 'HIGH'

def tactic():
    return 'Privilege Escalation (TA0004)'

def technique():
    return 'Access Token Manipulation (T1134)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}