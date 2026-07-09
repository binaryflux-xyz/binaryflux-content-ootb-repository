# Detection: Port Scan (Multiple Destination Ports from One Source)

def window():
    return "5m"

def groupby():
    return ['source_ip']

def algorithm(event_data):
    destinationportlist=stats.collect(['destination_port'])
    if event_data.get('network_protocol') in ['TCP', 'UDP']:
        print(destinationportlist)
        unique_ports = destinationportlist.get('destination_port', set())
        if len(unique_ports) > 5:
            return 1.0
    return 0.0

def context(event_data):
    return (
        "Potential port scan detected from source IP " + str(event_data.get('source_ip')) +
        " which attempted connections to over 5 distinct destination ports within 5 minutes."
    )

def criticality():
    return 'CRITICAL'

def tactic():
    return 'Discovery (TA0007)'

def technique():
    return 'Port Scanning (T1046)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip', 'destination_port','network_protocol'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
