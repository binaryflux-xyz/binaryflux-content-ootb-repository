def window():
    return '10s'


def groupby():
    return 'destination_ip'

def algorithm(event):
    
    if stats.count("source_ip") > 10:
        return 1.0


def context(event_data):

    destination_ip = event_data.get("destination_ip")
    return "DDoS WARNING: more than 10 different IPs are attacking "+destination_ip+" in 10 sec!"
    
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
                "destination_ip"
            ]
        )
    except Exception as e:
        raise e
