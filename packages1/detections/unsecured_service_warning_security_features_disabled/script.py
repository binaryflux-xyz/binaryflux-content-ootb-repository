# Detection: Unsecured Service Warning Security Features Disabled

def window():
    return None  # Instantaneous detection based on a single log event

def groupby():
    return None

def algorithm(event):
    message = str(event.get('event_message', '')).lower()
    keywords = [
        'security features are not enabled',
        'without authentication',
        'your cluster could be accessible to anyone'
    ]
    if any(keyword in message for keyword in keywords):
        return 0.75  # Strong indication of misconfiguration
    return 0.0

def context(event):
    return "A security misconfiguration was detected in component"+event.get('process_name')+ " thread "+event.get('process_thread_name')+"." +"The following message indicates an unsecured service:"+event.get('event_message')

def criticality():
    return 'HIGH'

def tactic():
    return 'Initial Access (TA0001)'

def technique():
    return 'Exploit Public-Facing Application (T1190)'

def artifacts():
    return stats.collect([
        'process_name',
        'process_thread_name',
        'event_severity',
        'event_message'
    ])

def entity(event):
    return {'derived': False, 'value': event.get('process_name'), 'type': 'application'}
