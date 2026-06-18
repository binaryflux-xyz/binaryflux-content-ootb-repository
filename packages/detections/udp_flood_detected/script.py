def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get("attack_type", "") == "UDP Flood" and float(event.get("bps", 0)) > 500000000:
        return 1.0
    return 0.0

def context(event):
    return "This detection triggered because a UDP Flood attack was observed and traffic volume exceeded 500000000 BPS. Target=%s, Current BPS=%s. This may indicate bandwidth saturation or volumetric denial-of-service activity." % (
        event.get("destination_ip", "unknown"),
        event.get("bps", 0)
    )

def criticality():
    return "CRITICAL"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Endpoint Denial of Service (T1499)"

def entity(event):
    return {"derived": False, "value": event.get("destination_ip"), "type": "ipaddress"}