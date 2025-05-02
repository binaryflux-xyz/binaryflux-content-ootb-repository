
UDP_THRESHOLD = 1000  # More than 1000 UDP packets in 10s

def window():
    return '10s'

def groupby():
    return 'source_ip'


def algorithm(event):
    '''
    proto == 17 means UDP --> Indicates UDP traffic
    '''
    proto = None
    
    try:
        if event.get('details').get("proto") is not None :
            proto = int(event.get('details').get("proto"))
    except Exception as e:
        pass

    if proto is not None and proto == 17 and event.get('network_packets_out') > 0 :
            if stats.count("source_ip") > UDP_THRESHOLD:
                return 1.0


def context(event_data):

    source_ip = event_data.get("source_ip")
    
    return "UDP FLOOD DETECTED: "+source_ip+" sent more than 1000 UDP packets in 10 sec!"
    
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
