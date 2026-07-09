def window():
    return None

def groupby():
    return None

def algorithm(event):
    protocol = event.get("protocol", "")
    pps = float(event.get("pps", 0))
    bps = float(event.get("bps", 0))

    if protocol == "UDP" and pps > 0 and bps > (pps * 500):
        return 0.75
    return 0.0

def context(event):
    return "This detection triggered because UDP traffic showed unusually high bandwidth relative to packet count. Target=%s, PPS=%s, BPS=%s. This pattern is commonly associated with reflection or amplification attacks." % (
        event.get("destination_ip", "unknown"),
        event.get("pps", 0),
        event.get("bps", 0)
    )

def criticality():
    return "HIGH"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Network Denial of Service (T1498)"

def entity(event):
    return {"derived": False, "value": event.get("destination_ip"), "type": "ipaddress"}