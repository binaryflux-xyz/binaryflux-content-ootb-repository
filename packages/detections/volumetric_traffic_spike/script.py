def window():
    return None

def groupby():
    return None

def algorithm(event):
    pps = float(event.get("pps", 0))
    bps = float(event.get("bps", 0))

    if pps > 1000000 or bps > 1000000000:
        return 0.75
    return 0.0

def context(event):
    return "This detection triggered because traffic exceeded volumetric thresholds. PPS=%s, BPS=%s, Target=%s. Such spikes may indicate flood activity or abnormal traffic surges impacting availability." % (
        event.get("pps", 0),
        event.get("bps", 0),
        event.get("destination_ip", "unknown")
    )

def criticality():
    return "HIGH"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Network Denial of Service (T1498)"

def entity(event):
    return {"derived": False, "value": event.get("destination_ip"), "type": "ipaddress"}