# Detection: High Volume External Network Transfer (>5 MB)

def window():
    return "5m"

def groupby():
    return ['interface_id']

def algorithm(event_data):
    total = stats.sum('total_bytes_transferred')
    src = event_data.get('source_ip', '')
    if not src.startswith("10.") and total > 100 * 1024 * 1024:  # 100 MB
        return 0.75
    return 0.0

def context(event):
    return "External network transfer exceeded 100 MB from %s to %s within 5 minutes." % (
        event.get('source_ip', 'N/A'),
        event.get('destination_ip', 'N/A')
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Exfiltration (TA0010)'

def technique():
    return 'Exfiltration Over C2 Channel (T1041)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
