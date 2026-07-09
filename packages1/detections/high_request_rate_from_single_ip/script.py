
def window():
    return '10s'

def groupby():
    return 'source_ip'


def algorithm(event):

    if stats.count("source_ip") > 100:
        return 1.0


def context(event_data):

    source_ip = event_data.get("source_ip")
    return "HIGH REQUEST RATE DETECTED: "+source_ip+" sent more than 100 requests in 10 sec!"
    
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
                "source_ip"
            ]
        )
    except Exception as e:
        raise e
