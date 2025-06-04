def window():
    return '5m'
    
def groupby():
    return ['source_ip']
    
def algorithm(event_data):
    destinationportlist=stats.collect(['destination_port'])
    if event_data['event_type'] == 'firewall_log' and event_data.get('network_protocol') in ['TCP', 'UDP']:
        print(destinationportlist)
        unique_ports = destinationportlist.get('destination_port', set())
        print(unique_ports)
        if len(unique_ports) > 5:
            return 1.0
    return 0.0
    
def context(event_data):
    return (
        "Potential port scan detected from source IP " + str(event_data.get('source_ip', 'unknown')) +
        " which attempted connections to over 5 distinct destination ports within 5 minutes."
    )
    
def criticality():
    return 'CRITICAL'
    
def tactic():
    return 'Reconnaissance (TA0043)'
    
def technique():
    return 'Port Scanning (T1046)'
    
def artifacts():
    return stats.collect(['source_ip', 'destination_port', 'network_protocol', 'event_type'])
    
def entity(event):
    return {'derived': False,
            'value': event['source_ip'],
            'type': 'ipaddress'}