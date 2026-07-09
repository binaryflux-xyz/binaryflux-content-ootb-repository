def window():
    # No aggregation needed, event-level detection
    return None

def groupby():
    return None

def is_valid_number(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str) and value.strip().replace('.', '', 1).isdigit():
        return True
    return False

def algorithm(event):
    """
    Detects high packet rate in short sessions by summing network_packets_in and network_packets_out.
    Heuristic: total packets > 50 and session duration < 10 seconds.
    """

    packets_in_raw = event.get('network_packets_in', 0)
    packets_out_raw = event.get('network_packets_out', 0)
    duration_raw = event.get('event_duration', 0)

    packets_in = int(packets_in_raw) if is_valid_number(packets_in_raw) else 0
    packets_out = int(packets_out_raw) if is_valid_number(packets_out_raw) else 0
    duration = float(duration_raw) if is_valid_number(duration_raw) else 0.0

    total_packets = packets_in + packets_out

    if total_packets > 50 and 0 <= duration < 10:
        return 0.75  # High risk score

    return 0.0

def context(event):
    packets_in = event.get('network_packets_in', 'N/A')
    packets_out = event.get('network_packets_out', 'N/A')
    duration = event.get('event_duration', 'N/A')
    src_ip = event.get('source_ip', 'N/A')
    dst_ip = event.get('destination_ip', 'N/A')

    return ("High packet rate detected in short session: total packets in = " + str(packets_in) +
            ", packets out = " + str(packets_out) +
            ", session duration = " + str(duration) + " seconds. " +
            "Source IP: " + src_ip + ", Destination IP: " + dst_ip + ".")

def criticality():
    return 'HIGH'

def tactic():
    return 'Execution (TA0002)'

def technique():
    return 'Network Service Scanning (T1046)'

def artifacts():
    return stats.collect(['network_packets_in', 'network_packets_out', 'event_duration', 'source_ip', 'destination_ip'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip', 'unknown'), 'type': 'ip_address'}
