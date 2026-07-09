def window():
    return None
def groupby():
    return None
def algorithm(event):
    if event['event_id'] == 10 and 'lsass.exe' in event['target_process']:
        return 0.95
    return None
def context(event_data):
    return "Process " + event_data['process_name'] + " accessed LSASS memory, possible credential dumping attempt."
def criticality():
    return 'CRITICAL'
def tactic():
    return 'Credential Access (TA0006)'
def technique():
    return 'OS Credential Dumping (T1003)'
def artifacts():
    return stats.collect(['process_name', 'target_process', 'event_id'])
def entity(event):
    return {'derived': False, 'value': event['process_name'], 'type': 'process'}