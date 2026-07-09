def window():
    return None
def groupby():
    return None
def algorithm(event):
    if event['event_id'] == 4688 and 'powershell.exe' in event['process_name']:
        suspicious_keywords = ['DownloadString', 'IEX', 'Invoke-Expression', 'bypass']
        for keyword in suspicious_keywords:
            if keyword in event['command_line']:
                return 0.85
    return 0.0
def context(event_data):
    return "Suspicious PowerShell command executed: " + event_data['command_line']
def criticality():
    return 'HIGH'
def tactic():
    return 'Execution (TA0002)'
def technique():
    return 'PowerShell (T1059.001)'
def artifacts():
    return stats.collect(['process_name', 'command_line'])
def entity(event):
    return {'derived': False, 'value': event['process_name'], 'type': 'process'}