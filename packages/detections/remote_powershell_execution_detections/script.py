def window():
    return None

def groupby():
    return None

def algorithm(event):
    # Detecting Remote PowerShell Execution
    if event.get('event_id') in [4104, 4648, 4688]:
        if 'powershell.exe' in event.get('process_name', '').lower():
            if '-EncodedCommand' in event.get('command_line', '') or 'Invoke-Expression' in event.get('command_line', ''):
                return 0.9  # High confidence for encoded or suspicious PowerShell execution
            if event.get('logon_type') == 3:  # Remote login detected
                return 0.85  # Remote PowerShell execution detected

    return None

def context(event_data):
    return "Potential Remote PowerShell Execution detected from {0} by {1}. Command: {2}".format(
        event_data.get('source_ip', 'Unknown IP'),
        event_data.get('user_name', 'Unknown User'),
        event_data.get('command_line', 'N/A')
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Lateral Movement (TA0008)'

def technique():
    return 'Remote Services: PowerShell (T1021.006)'

def artifacts():
    return stats.collect(['event_id', 'process_name', 'command_line', 'source_ip', 'user_name', 'logon_type'])

def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip', 'Unknown IP'),
        'type': 'host'
    }
