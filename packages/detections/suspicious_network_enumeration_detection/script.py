def window():
    return '5m'  # Analyze network activity within a 5-minute window

def groupby():
    return ['source_ip']  # Grouping by internal scanning source

def algorithm(event):
    # Detecting internal network enumeration activity
    if event.get('event_id') == 5156:  # Windows Filtering Platform logs allowed connections
        recon_ports = [135, 139, 445, 389, 3389, 22]  # SMB, LDAP, RDP, SSH (commonly scanned)
        
        destination_port = event.get('destination_port')
        destination_ip = event.get('destination_ip')
        
        # Exclude external connections; focus on internal scanning (e.g., 192.168.x.x, 10.x.x.x)
        if destination_ip.startswith(('192.168.', '10.', '172.16.')) and destination_port in recon_ports:
            return 0.85  # High confidence for internal reconnaissance activity

    return None

def context(event_data):
    return "Potential Network Enumeration Detected! Source: {0}, Target: {1}, Port: {2}".format(
        event_data.get('source_ip', 'Unknown'),
        event_data.get('destination_ip', 'Unknown'),
        event_data.get('destination_port', 'N/A')
    )

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Lateral Movement & Reconnaissance (TA0008)'

def technique():
    return 'Remote System Discovery (T1018)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip', 'destination_port', 'event_id'])

def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip', 'Unknown'),
        'type': 'network'
    }
