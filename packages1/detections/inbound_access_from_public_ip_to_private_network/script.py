# Detection: Inbound Connection from Public IP to Private IP (Python 2)

def window():
    return '1d'

def groupby():
    return ['source_ip']

def algorithm(event):
    src = event.get('source_ip', '')
    dst = event.get('destination_ip', '')
    if not src.startswith('10.') and dst.startswith('10.'):
        if(stats.getcount(event.get('source_ip')) <=0):
          stats.count(event.get('source_ip'))
          return 0.75  # Potential external access to internal system
        else:
          return 0.0
    return 0.0

def context(event):
    src = event.get('source_ip', 'N/A')
    dst = event.get('destination_ip', 'N/A')
    return (
        "External IP %s attempted to access internal private IP %s. "
        "This may indicate unauthorized or suspicious inbound traffic." %
        (src, dst)
    )

def criticality():
    return 'HIGH'

def tactic():
    return 'Initial Access (TA0001)'

def technique():
    return 'Exploit Public-Facing Application (T1190)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
