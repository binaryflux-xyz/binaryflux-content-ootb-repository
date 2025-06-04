def window():
    return '5m'
def groupby():
    return 'account_name'
def algorithm(event):
    dangerous = ['xp_cmdshell', 'sp_OACreate', 'bcp', 'powershell']
    for keyword in dangerous:
        if keyword in event['statement'].lower():
            return 0.95
    return 0.0
def context(event_data):
    return (
        "Suspicious system-level function used by " + event_data['account_name'] +
        ": " + event_data['statement']
    )
def criticality():
    return 'HIGH'
def tactic():
    return 'Execution (TA0002)'
def technique():
    return 'Command and Scripting Interpreter (T1059)'
def artifacts():
    return stats.collect(['account_name', 'statement', 'client_ip', 'timestamp'])
def entity(event):
    return {'derived': False, 'value': event['account_name'], 'type': 'user'}
