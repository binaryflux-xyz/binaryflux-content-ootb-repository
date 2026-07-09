def window():
    return '1m'
def groupby():
    return 'source_ip'
def algorithm(event):
    if event['process_command_line'].lower().startswith('alter server audit') or 'disable audit' in event['process_command_line'].lower():
        return 1.0
    return 0.0
def context(event_data):
    return (
        "Audit configuration was modified by account ip: "
        + event_data['source_ip'] + " via statement: " + event_data['process_command_line']
    )
def criticality():
    return 'CRITICAL'
def tactic():
    return 'Defense Evasion (TA0005)'
def technique():
    return 'Indicator Removal on Host (T1070)'
def artifacts():
    return stats.collect(['user_name', 'process_command_line',  'source_ip'])
def entity(event):
    return {'derived': False, 'value': event['user_name'], 'type': 'user'}