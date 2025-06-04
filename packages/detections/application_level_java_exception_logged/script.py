# Detection: Application Error Severity Logged

def window():
    return None  # Instantaneous detection based on a single log event

def groupby():
    return None
  

def algorithm(event):
    message = str(event.get('event_message', '')).lower()
    if "exception" in message and "org." in message:
        return 0.75  # High confidence: likely Java stacktrace or error
    return 0.0

def context(event):
    return (
        "Exception traceback logged from runtime:\n"
        "- Details: {}\n"
        "- Module: {}\n"
        "- Thread: {}\n"
        "- Severity: {}"
    ).format(
        event.get('event_message', 'N/A'),
        event.get('process_name', 'unknown'),
        event.get('process_thread_name', 'unknown'),
        event.get('event_severity', 'INFO')
    )

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Impact (TA0040)'

def technique():
    return 'Data Manipulation (T1565.001)'

def artifacts():
    return stats.collect([
        'process_name',
        'process_thread_name',
        'event_severity'
    ])

def entity(event):
    return {'derived': False, 'value': event.get('process_name'), 'type': 'application'}
