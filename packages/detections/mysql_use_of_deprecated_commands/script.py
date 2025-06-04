def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '')
    risky_commands = ['FLUSH PRIVILEGES', 'FLUSH TABLES', 'KILL', 'RESET MASTER', 'RESET SLAVE']
    
    if any(cmd in argument for cmd in risky_commands):
        return 0.75  
    return 0.0

def context(event_data):
    user = str(event_data.get('user_host', 'unknown'))
    command = str(event_data.get('argument', 'N/A'))
    return "Dangerous command '{}' was executed by {}".format(command, user)

def criticality():
    return 'High'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Indicator Removal on Host (T1070)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}