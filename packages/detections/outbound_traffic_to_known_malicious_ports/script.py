def window():
    return None

def groupby():
    return None

def algorithm(event):
    malicious_ports = ['4444', '1337', '12345', '6667', '31337']
    malicious_udp_ports = ['12345', '31337']

    src_zone = event.get('source_zone')
    dst_zone = event.get('destination_zone')
    dst_port = event.get('destination_port')
    proto = event.get('details', {}).get('proto')

    # Only consider Internal to External traffic
    if src_zone == 'Internal' and dst_zone == 'External':
        # Check TCP or UDP malicious ports
        if dst_port in malicious_ports or (proto == '17' and dst_port in malicious_udp_ports):
            return 1.0

    return 0.0

def context(event):
    return (
        'Internal host ' + str(event.get('source_ip')) +
        ' attempted to connect to external IP ' + str(event.get('destination_ip')) +
        ' over potentially malicious port ' + str(event.get('destination_port')) +
        ' (protocol: ' + str(event.get('details', {}).get('proto')) + ').'
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Command and Control (TA0011)'

def technique():
    return 'Application Layer Protocol (T1071)'

def artifacts():
    return stats.collect([
        'source_ip',
        'destination_ip',
        'destination_port',
        'proto',
        'source_zone',
        'destination_zone',
        'rule',
        'product_name',
        'product_family',
        'network_application'
    ])

def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip'),
        'type': 'ipaddress'
    }
