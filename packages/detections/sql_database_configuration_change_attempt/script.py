def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get('event_type') == 'INFO' and 'Setting database option' in event.get('Message', ''):
        return 0.50
    elif event.get('action_id', '').strip() in ['CR', 'AL', 'DR'] and event.get('statement', '').startswith('ALTER DATABASE'):
        return 0.50
    return 0.0



def context(event):
    if event.get('event_type') == 'INFO':
      return (event['Message'])
    else:
      return 'Database Permissions were changes by ' + str(event.get('statement', '')) + ' on database ' + str(event.get('database_name', ''))

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Persistence (TA0003)'

def technique():
    return 'Event Triggered Execution (T1546)'

def artifacts():
    return stats.collect(['database_name', 'schema_name', 'server_initiated_user_name', 'action_name', 'event_type'])

def entity(event):
    return {'derived': False, 'value': event['server_principal_name'], 'type': 'accountname'}
