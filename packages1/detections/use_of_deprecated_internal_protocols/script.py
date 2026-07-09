def window():
    return '5m'

def groupby():
    return ['source_ip', 'destination_ip']

def algorithm(event):
    src_zone = event.get('source_zone')
    dst_zone = event.get('destination_zone')
    service = str(event.get('network_application')).lower()
    proto = str(event.get('details', {}).get('proto')).lower()

    deprecated_services = ['telnet', 'ftp', 'netbios']
    deprecated_protocols = ['tcp/23', 'tcp/21', 'udp/137', 'udp/138', 'tcp/139']

    if src_zone == 'Internal' and dst_zone == 'Internal':
        for d in deprecated_services:
            if d in service:
                return 0.5
        if proto in deprecated_protocols:
            return 0.5

    return 0.0

def context(event):
    return (
        'Internal communication from ' + str(event.get('source_ip')) +
        ' to ' + str(event.get('destination_ip')) +
        ' using potentially deprecated service or protocol: ' +
        str(event.get('network_application'))
    )

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Lateral Movement (TA0008)'

def technique():
    return 'Exploitation of Remote Services (T1210)'

def artifacts():
    return stats.collect([
        'source_ip',
        'destination_ip',
        'source_zone',
        'destination_zone',
        'network_application',
        'details.proto',
        'product_name',
        'product_family'
    ])

def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip'),
        'type': 'ipaddress'
    }
