# Detection: Suspicious Protocol Usage (e.g., ICMP, GRE, ESP, AH)

def window():
    return None

def groupby():
    return None

def algorithm(event):
    protocol = str(event.get('network_protocol', '')).upper()
    if protocol in ['ICMP', 'GRE', 'ESP', 'AH']:
        return 0.5
    return 0.0

def context(event):
    protocol = str(event.get('network_protocol', 'N/A')).upper()
    src = event.get('source_ip', 'N/A')
    dst = event.get('destination_ip', 'N/A')
    return (
        "Suspicious protocol %s detected in a connection from source IP %s to destination IP %s. "
        "This may indicate use of tunneling or non-standard communication for command and control." %
        (protocol, src, dst)
    )

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Command and Control (TA0011)'

def technique():
    return 'Application Layer Protocol (T1071)'

def artifacts():
    return stats.collect(['network_protocol', 'source_ip', 'destination_ip'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
