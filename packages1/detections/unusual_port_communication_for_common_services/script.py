def window():
    return None

def groupby():
    return None

def algorithm(event):
    common_ports = {
        'http': '80', 'https': '443', 'dns': '53'
    }
    service = event.get('network_application', '')
    if service:
      service = service.lower()
      port = event.get('destination_port')
      if service in common_ports and port != common_ports[service]:
          return 0.7
    return 0.0

def context(event):
    return 'Service {} used non-standard port {} between {} and {}'.format(
        event.get('network_application'),
        event.get('destination_port'),
        event.get('source_ip'),
        event.get('destination_ip')
    )

def criticality():
    return 'MEDIUM'

def tactic():
    return 'Command and Control (TA0011)'

def technique():
    return 'Application Layer Protocol (T1071)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip', 'network_application', 'destination_port'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
