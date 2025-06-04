def window():
    # Use a time window for aggregation, e.g., 5 minutes
    return None

def groupby():
    # Group by source IP and destination IP to monitor data flow between hosts
    return None

def algorithm(event):
    """
    Calculate a risk score for possible data exfiltration.
    Heuristic: Large outbound data volume (network_bytes_out) to external IPs (not in private IP ranges)
    """
    bytes_out_str = event.get('network_bytes_out', '0')
    dest_ip = event.get('destination_ip', '')

    # Convert bytes_out_str to int if possible, else 0
    bytes_out = 0
    if bytes_out_str and all(c in '0123456789' for c in bytes_out_str):
        bytes_out = int(bytes_out_str)

    ip_parts = dest_ip.split('.')
    if len(ip_parts) == 4:
        first_octet = ip_parts[0]
        second_octet = ip_parts[1]

        if (first_octet != '10' and
            first_octet != '192' and
            not (first_octet == '172' and int(second_octet) >= 16 and int(second_octet) <= 31)):
            
            if bytes_out > 100000:
                return 0.75

    return 0.0


def context(event):
    # Narrative explanation of the detection event
    return ("Detected possible data exfiltration from source IP " + event.get('source_ip') +
            " to external destination IP " + event.get('destination_ip') +
            ". Outbound data volume is approximately " + event.get('network_bytes_out', '0') +
            " bytes over the last 5 minutes. Monitor this activity for potential data leak.")

def criticality():
    return 'HIGH'

def tactic():
    return 'Exfiltration (TA0010)'

def technique():
    return 'Data Transfer Size Limits (T1030)'

def artifacts():
    # List important fields to store for further analysis
    return stats.collect(['source_ip', 'destination_ip', 'network_bytes_out', 'network_packets_out', 'application', 'rule'])

def entity(event):
    # Derive entity: source IP as endpoint of interest
    return {'derived': True, 'type': 'ip', 'value': event.get('source_ip', 'unknown')}
