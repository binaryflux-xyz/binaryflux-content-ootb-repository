def window():
    return None

def groupby():
    return None

def algorithm(event):
    argument = event.get('argument', '')

    suspicious_keywords = ['JOIN', 'UNION', 'EXISTS', 'IN (SELECT']
    if any(kw in argument for kw in suspicious_keywords):
        return 0.50  # Moderate confidence
    return 0.0


def context(event_data):
    user_host = event_data.get('user_host', 'unknown')
    query = event_data.get('argument', 'N/A')

    return "Suspicious query involving JOINs or subqueries detected from {}. Query: \"{}\"".format(user_host, query)



def criticality():
    return 'Medium'

def tactic():
    return 'Collection (TA0009)'

def technique():
    return 'Data from Information Repositories (T1213)'

def artifacts():
    return stats.collect(['user_host', 'command_type'])

def entity(event):
    return {'derived': False, 'value': event['user_host'], 'type': 'hostname'}