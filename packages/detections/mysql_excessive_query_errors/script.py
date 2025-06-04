def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '').upper()
    error_signatures = ['UNKNOWN TABLE', 'ACCESS DENIED', 'SYNTAX ERROR', 'UNKNOWN COLUMN']
    if any(err in argument for err in error_signatures):
        return 0.75  
    return 0.0



def context(event_data):
    user_host = event_data.get('user_host', 'unknown')
    argument = event_data.get('argument', '').upper()

    if 'UNKNOWN TABLE' in argument:
        return "Query on unknown table from {}: {}".format(user_host, argument)
    elif 'ACCESS DENIED' in argument:
        return "Access denied error from {}: {}".format(user_host, argument)
    elif 'SYNTAX ERROR' in argument:
        return "Syntax error in query from {}: {}".format(user_host, argument)
    elif 'UNKNOWN COLUMN' in argument:
        return "Query referencing unknown column from {}: {}".format(user_host, argument)
    else:
        return "Excessive query errors detected on {}: {}".format(user_host, argument)


def criticality():
    return 'High'

def tactic():
    return 'Discovery (TA0007)'

def technique():
    return 'System Information Discovery (T1082)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}