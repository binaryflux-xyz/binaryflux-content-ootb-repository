from datetime import datetime, timedelta


def window():
    return '5m'


def groupby():
    return ['source_ip']

def investigate():
    return "palo_alto_network_traffic_intelligence"

def automate():
    return True

def _event_hour(event):
    ts = event.get('timestamp')
    if not ts:
        return None

    try:
        dt = datetime.utcfromtimestamp(int(ts) / 1000.0) + timedelta(hours=5, minutes=30)
        return dt.hour
    except Exception:
        return None


def algorithm(event):
    timestamp = event.get('timestamp')
    bytes_out = event.get('network_bytes_out')
    action = (event.get('event_action') or '').lower()
    src = event.get('source_ip')
    dst = event.get('destination_ip')
  
    if not timestamp or not bytes_out:
        return 0.0

    if action not in ['allow', 'accept', 'permit']:
        return 0.0
    
    if (src.startswith("10.") or src.startswith("192.168.") or src.startswith("172.")):
      if not (dst.startswith("10.") or dst.startswith("192.168.") or dst.startswith("172.")):
          hour = _event_hour(event)
          if hour is None:
              return 0.0
          
          bytes_out = int(bytes_out)
          total_bytes = stats.sum("network_bytes_out")
          if hour >= 22 or hour < 8:
              if total_bytes and int(total_bytes) > 1073741824:
                  return 0.75
    return 0.0


def context(event_data):
    return (
        'Unusual data transfer detected from source IP '
        + str(event_data.get('source_ip'))
        + ' to one of the destination IPs '
        + str(event_data.get('destination_ip'))
        + ' during off-hours. A total of '
        + str(stats.resetsum("network_bytes_out"))
        + ' bytes were transferred within 5-minutes interval.'
    )


def criticality():
    return 'HIGH'


def tactic():
    return 'Exfiltration (TA0010)'


def technique():
    return 'Exfiltration Over Network (T1041)'


def artifacts():
    return stats.collect([
        'source_ip',
        'destination_ip',
        'network_bytes_out',
        'destination_port',
        'network_protocol',
        'eventreceivedtime'
    ])


def entity(event):
    return {
        'derived': False,
        'value': event.get('source_ip'),
        'type': 'ipaddress'
    }
