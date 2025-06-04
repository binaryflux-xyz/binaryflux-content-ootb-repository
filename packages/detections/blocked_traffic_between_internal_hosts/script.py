def window():
    return '5m'  # 5-minute window for analysis

def groupby():
    return ['source_ip']  # Group by source and destination IP

def algorithm(event):
    src_zone = event.get('source_zone')
    dst_zone = event.get('destination_zone')
    action = event.get('event_action')
    
    # Only consider drops between internal zones
    if src_zone == 'Internal' and dst_zone == 'Internal' and action == 'drop':
        if stats.count(event.get('destination_ip')) > 3:
            return 0.75

    return 0.0


def context(event):
    return (
        'Internal host ' + str(event.get('source_ip')) + 
        ' repeatedly attempted connections to internal host ' + str(event.get('destination_ip')) +
        ' but the traffic was blocked (dropped) by firewall rules.'
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Lateral Movement (TA0008)'

def technique():
    return 'Internal Spearphishing (T1071.001)'  # Adjusted technique for blocked internal communication


def artifacts():
    return stats.collect([
        'source_ip',
        'destination_ip',
        'source_zone',
        'destination_zone',
        'event_action',
        'rule',
        'product_name',
        'product_family'
    ])

def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip'),
        'type': 'ipaddress'
    }
