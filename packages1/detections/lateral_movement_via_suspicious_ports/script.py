def window():
    return '10m'  # 10-minute analysis window

def groupby():
    return ['source_ip']  # Group events by source IP

def algorithm(event):
    internal_zones = ['Internal', 'Local']
    suspicious_ports = ['135', '445', '3389', '22', '5985', '23', '21', 'rpc', 'rdp', 'smb', 'netbios', 'telnet']
    destinationportlist=stats.collect(['destination_ip'])
    unique_ports = destinationportlist.get('destination_port', set())

    src_zone = event.get('source_zone')
    dst_zone = event.get('destination_zone')
    dest_port = str(event.get('destination_port')).lower()
    service = str(event.get('network_application')).lower()

    if src_zone in internal_zones and dst_zone in internal_zones:
        if dest_port in suspicious_ports or service in suspicious_ports:
            if len(unique_ports) >3:
                return 0.75

    return 0.0


def context(event):
    return (
        'Possible lateral movement detected: Internal host ' + str(event.get('source_ip')) +
        ' connected to multiple internal systems using suspicious port/service "' +
        str(event.get('destination_port')) + '" or application "' +
        str(event.get('network_application')) + '".'
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Lateral Movement (TA0008)'

def technique():
    return 'Remote Services (T1021)'

def artifacts():
    return stats.collect([
        'source_ip',
        'destination_ip',
        'destination_port',
        'network_application',
        'source_zone',
        'destination_zone',
        'details.proto',
        'event_action',
        'rule',
        'product_name',
        'product_family'
    ])

def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip'),
        'type': 'ipaddress'
    }
