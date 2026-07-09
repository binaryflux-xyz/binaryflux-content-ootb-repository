# Detection: Application Error Severity Logged

def window():
    return None  # Instantaneous detection based on a single log event

def groupby():
    return None
  

def algorithm(event):
    severity = str(event.get('event_severity', '')).upper()
    if severity == 'ERROR':
        return 0.75  # High confidence in error severity as indicator
    return 0.0

def context(event):
    return (
        "An application log was captured with severity 'ERROR'. "
        "Component: " + event.get('process_name', 'unknown') +
        ", Thread: " + event.get('process_thread_name', 'unknown') + ". "
        "Log message: " + event.get('event_message', '')
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Execution (TA0002)'

def technique():
    return 'Application Layer Protocol (T1071)'

def artifacts():
    return stats.collect([
        'process_name',
        'process_thread_name',
        'event_severity',
        'event_message'
    ])

def entity(event):
    return {'derived': False, 'value': event.get('process_name'), 'type': 'application'}
