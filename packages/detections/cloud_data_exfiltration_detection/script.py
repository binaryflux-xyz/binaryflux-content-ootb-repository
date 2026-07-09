def window():
    return None

def groupby():
    return None

def algorithm(event):
    # Detects Cloud Uploads via network connections & file activity
    cloud_services = [
        'drive.google.com', 'dropbox.com', 'onedrive.live.com', 's3.amazonaws.com', 
        'mega.nz', 'box.com', 'icloud.com'
    ]

    if event.get('event_id') == 5156:  # Network connection event
        dest_ip = event.get('destination_ip', '')
        domain = event.get('destination_domain', '')

        # Check if the connection is to a known cloud storage service
        if any(service in domain.lower() for service in cloud_services):
            return 0.9  # High confidence score

    if event.get('event_id') == 5140:  # File share access (potential staging)
        if event.get('share_name', '').lower() in ['c$', 'admin$', 'ipc$']:
            return 0.75  # Possible file staging before upload

    return None

def context(event_data):
    return "Potential cloud data exfiltration detected. User: {0}, Destination: {1}, Process: {2}".format(
        event_data.get('user_name', 'Unknown User'),
        event_data.get('destination_domain', 'Unknown Destination'),
        event_data.get('process_name', 'Unknown Process')
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Command & Control (TA0011)'

def technique():
    return 'Exfiltration to Cloud Storage (T1567.002)'

def artifacts():
    return stats.collect(['event_id', 'destination_ip', 'destination_domain', 'process_name', 'user_name'])

def entity(event):
    return {
        'derived': False,
        'value': event.get('destination_domain', 'Unknown Destination'),
        'type': 'network'
    }
