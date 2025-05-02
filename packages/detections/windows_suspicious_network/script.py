def window():
    return '5m'  # Monitors traffic in a 5-minute window

def groupby():
    return ['destination_ip']  # Grouping by the external IP to track multiple connections

def algorithm(event):
    # Detecting outbound C2 communications based on destination port and frequency
    if event.get('event_id') == 5156:  # Windows Filtering Platform logs outbound connections
        suspicious_ports = [4444, 8080, 1337, 9001, 53]  # Common C2 ports (can be extended)
        known_good_ports = [80, 443, 22]  # Normal web and SSH traffic
        
        destination_port = event.get('destination_port')
        
        if destination_port in suspicious_ports and destination_port not in known_good_ports:
            return 0.9  # High confidence for C2 activity

    return None

def context(event_data):
    return "Suspicious C2 Network Activity Detected! Destination: {0}, Port: {1}".format(
        event_data.get('destination_ip', 'Unknown'),
        event_data.get('destination_port', 'N/A')
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Command and Control (TA0011)'

def technique():
    return 'Application Layer Protocol (T1071)'

def artifacts():
    return stats.collect(['destination_ip', 'destination_port', 'event_id'])

def entity(event):
    return {
        'derived': False,
        'value': event.get('destination_ip', 'Unknown'),
        'type': 'network'
    }
