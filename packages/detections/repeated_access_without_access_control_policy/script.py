def window():
    return '5m'  # Triggered on a single event

def groupby():
    return ['service_name','service_endpoint']  # No grouping needed

def algorithm(event):
    message = str(event.get('event_message', '')).lower()

    if "no access control policy" in message and "allowing access" in message:
        stats.count("nopolicy_access_control")  # Increment the counter first

        if stats.getcount("nopolicy_access_control") > 5:
            return 0.75  # Trigger detection if count exceeds 5

    return 0.0  # No match or below threshold

def context(event):
    service = event.get('service_name')
    endpoint = event.get('service_endpoint')
    thread = event.get('process_thread_name')
    component = event.get('process_name')
    severity = event.get('event_severity')

    return (
        "Over a 5-minute window, multiple access attempts were allowed to the service '{}' "
        "at endpoint '{}' without any access control policy in place. This behavior was logged "
        "by the '{}' component on thread '{}', with a severity level of '{}'.\n\n"
        "This repeated pattern suggests a potential security misconfiguration or an attempt "
        "to bypass access restrictions."
    ).format(service, endpoint, component, thread, severity)

def criticality():
    return 'HIGH'

def tactic():
    return 'Defense Evasion (TA0005)'

def technique():
    return 'Impair Defenses (T1562.001)'

def artifacts():
    return stats.collect([
        'process_name',
        'process_thread_name',
        'service_name',
        'service_endpoint',
        'event_severity'
    ])

def entity(event):
    service_name = details.get('service_name')

    return {
        'derived': False,
        'value': service,
        'type': 'service_name'
    }