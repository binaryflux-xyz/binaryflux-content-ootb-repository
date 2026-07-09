
SLOWLORIS_DURATION = 300  # Connections lasting >5 minutes

def window():
    return '10m'

def groupby():
    return 'source_ip'


def algorithm(event):
    '''
    proto == 6 means TCP --> Indicates TCP traffic
    action == accept (only SYN seen, no completion) --> Firewall accepted SYN packet
    sentpackets == 0 or very low --> No data sent after SYN (no full handshake)
    duration == 0 or very low --> Connection not completed
    '''
    proto = None
    duration = int(event.get('event_duration'))
    
    try:
        if event.get('details').get("proto") is not None :
            proto = int(event.get('details').get("proto"))
    except Exception as e:
        pass

    if proto is not None and proto == 6 and event.get('destination_port') in ["80","443"] and duration> SLOWLORIS_DURATION:
            if stats.count("source_ip") > 10:  # More than 10 slow connections
                return 1.0

def context(event_data):

    source_ip = event_data.get("source_ip")
    return "SLOWLORIS ATTACK DETECTED: "+source_ip+" has more than 10 long-lived connections!"
    
def criticality():
    return "HIGH"


def tactic():
    return "Impact (TA0040)"


def technique():
    return "Network Denial of Service (T1498)"


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}


def artifacts():
    try:
        return stats.collect(
            [
                "source_ip",
                "event_duration"
            ]
        )
    except Exception as e:
        raise e
