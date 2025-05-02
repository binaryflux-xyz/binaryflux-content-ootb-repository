
SYN_THRESHOLD = 50  # More than 50 half-open SYNs per IP

def window():
    return '10s'

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
    
    try:
        if event.get('details').get("proto") is not None :
            proto = int(event.get('details').get("proto"))
    except Exception as e:
        pass

    if proto is not None and proto == 6 and event.get('event_action') == "accept" and event.get('network_packets_out') <= 10 and event.get('event_duration') == 0:
            if stats.count("source_ip") > SYN_THRESHOLD:
                return 1.0


def context(event_data):

    source_ip = event_data.get("source_ip")
    
    return "SYN FLOOD DETECTED: "+source_ip+" sent more than 50 half-open SYN packets in 10 sec!"
    
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
                "proto",
                "network_packets_out",
                "event_duration"
            ]
        )
    except Exception as e:
        raise e
