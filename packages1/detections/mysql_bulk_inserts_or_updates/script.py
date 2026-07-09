def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '')
    if argument.startswith('INSERT') or argument.startswith('UPDATE'):
        return 0.75
    return 0.0

def context(event_data):
    user_host = event_data.get('user_host', 'unknown')
    argument = event_data.get('argument', '')

    if argument.startswith('INSERT'):
        return "Bulk INSERT activity detected from {}: {}".format(user_host, argument)
    elif argument.startswith('UPDATE'):
        return "Bulk UPDATE activity detected from {}: {}".format(user_host, argument)



def criticality():
    return 'High'

def tactic():
    return 'Impact (TA0040)'

def technique():
    return 'Data Manipulation (T1565)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}