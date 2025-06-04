def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '')
    keywords = ['ALTER TABLE', 'DROP COLUMN', 'CREATE TABLE', 'DROP TABLE', 'MODIFY COLUMN']

    if any(k in argument for k in keywords):
        if stats.count(event.get("user_host")) > 5:
            return 0.50  
    return 0.0

def context(event_data):
    user = str(event_data.get('user_host', 'unknown'))
    query = str(event_data.get('argument', 'N/A'))
    return "Frequent schema change detected from {}: {}".format(user, query)


def criticality():
    return 'Medium'

def tactic():
    return 'Impact (TA0040)'

def technique():
    return 'Data Manipulation (T1565)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}