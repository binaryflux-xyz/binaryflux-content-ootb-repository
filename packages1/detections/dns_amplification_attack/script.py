
DNS_AMP_RATIO = 5  # DNS response should not exceed 5x request size

def window():
    return None


def groupby():
    return None


def algorithm(event):

    proto = None
    sentbytes = int(event.get('network_bytes_out'))
    receivedbytes = int(event.get('network_bytes_in'))
    try:
        if event.get('details').get("proto") is not None :
            proto = int(event.get('details').get("proto"))
    except Exception as e:
        pass

    if proto is not None and proto == 17 and event.get('destination_port') == "53" and sentbytes > 1000 and receivedbytes > DNS_AMP_RATIO * sentbytes:
        return 1.0
      
def context(event_data):

    destination_ip = event_data.get("destination_ip")
    receivedbytes = int(event.get('network_bytes_in'))

    return "DNS AMPLIFICATION DETECTED: "+destination_ip+" received response "+event.get('network_bytes_in')+" bytes (5x request) from "+event_data.get("source_ip")
    
def criticality():
    return "CRITICAL"


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
                "destination_ip",
                "network_bytes_out",
                "network_bytes_out"
            ]
        )
    except Exception as e:
        raise e
