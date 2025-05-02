def window():
    return None

def groupby():
    return None

def algorithm(event):
    # Detecting shadow copy deletion via command execution
    if event.get('event_id') in [4104, 4688, 1]:  # PowerShell, Process Creation, Sysmon Process Create
        command = event.get('command_line', '').lower()
        
        shadow_copy_deletion_cmds = [
            'vssadmin delete shadows', 
            'wbadmin delete catalog', 
            'bcdedit /set {default} recoveryenabled no', 
            'wmic shadowcopy delete','wmic shadowcopy delete'
        ]
        
        if any(cmd in command for cmd in shadow_copy_deletion_cmds):
            return 0.95  # Very high confidence for shadow copy deletion

    return None

def context(event_data):
    return "Potential Shadow Copies Deletion Detected! Process: {0}, User: {1}, Command: {2}".format(
        event_data.get('process_name', 'Unknown Process'),
        event_data.get('user_name', 'Unknown User'),
        event_data.get('command_line', 'N/A')
    )

def criticality():
    return 'CRITICAL'

def tactic():
    return 'Data Destruction & Ransomware (TA0040)'

def technique():
    return 'Inhibit System Recovery (T1490)'

def artifacts():
    return stats.collect(['event_id', 'process_name', 'command_line', 'user_name'])

def entity(event):
    return {
        'derived': False,
        'value': event.get('process_name', 'Unknown Process'),
        'type': 'process'
    }
