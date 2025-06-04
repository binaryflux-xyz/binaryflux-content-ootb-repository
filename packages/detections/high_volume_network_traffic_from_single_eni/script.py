# Detection: High Volume Network Traffic from Single ENI (Python 2)

def window():
    return "5m"

def groupby():
    return ['interface_id']


def algorithm(event_data):
    total = stats.sum('total_bytes_transferred')
    interface_id=event_data.get("interface_id")
    src = event_data.get('source_ip')
    # print("Total"+str(total)+"for interfacid"+str(interface_id)+"and sourceip"+str(src))  # Print statement added

    if total > 2 * 1024 * 1024 * 1024:  # 5 MB threshold
        return 1
    return 0.0

def context(event):
    bytes_transferred = event.get('total_bytes_transferred', 'N/A')
    src = event.get('source_ip', 'N/A')
    dst = event.get('destination_ip', 'N/A')
    return (
        "High traffic volume detected: %s bytes transferred from source IP %s to destination IP %s "
        "within a 5-minute window exceeding the 2GB threshold. This may indicate possible data exfiltration." %
        (bytes_transferred, src, dst)
    )


def criticality():
    return 'CRITICAL'

def tactic():
    return 'Exfiltration (TA0010)'

def technique():
    return 'Exfiltration Over C2 Channel (T1041)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
