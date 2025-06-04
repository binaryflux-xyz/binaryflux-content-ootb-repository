def window():
    return '10m'

def groupby():
    return ['user_host']

def algorithm(event, stats):
    argument = event.get('argument', '').upper()

    if argument.startswith('SELECT'):
        if stats.get(event.get('user_host')) >= 5:
            return 0.75 
    return 0.0


def context(event_data):
    return "{} was attempted on the table by {}".format(
        event_data.get('argument', 'Unknown query'),
        event_data.get('user_host', 'unknown host')
    )


def criticality():
    return 'High'

def tactic():
    return 'Collection (TA0009)'

def technique():
    return 'Data from Information Repositories (T1213)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}