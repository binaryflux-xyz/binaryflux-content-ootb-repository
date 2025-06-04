def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '')
    keywords = ['SET NAMES', 'CHARACTER_SET_CLIENT', 'COLLATION_CONNECTION']

    if any(kw in argument for kw in keywords):
        return 0.50  
    return 0.0

def context(event_data):
    user = str(event_data.get('user_host', 'unknown'))
    cmd = str(event_data.get('argument', 'N/A'))
    return "Unexpected charset or collation change executed by {}: {}".format(user, cmd)

def criticality():
    return 'Medium'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Obfuscated Files or Information (T1027)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}