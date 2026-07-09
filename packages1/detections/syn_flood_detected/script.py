def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get("attack_type", "") == "SYN Flood" and float(event.get("pps", 0)) > 500000:
        return 1.0
    return 0.0

def context(event):
    return "This detection triggered because a SYN Flood attack was identified and packet rate exceeded 500000 PPS. Target=%s, Current PPS=%s. This may indicate an active TCP resource exhaustion attempt." % (
        event.get("destination_ip"),
        event.get("pps")
    )

def criticality():
    return "CRITICAL"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Network Denial of Service (T1498)"

def entity(event):
    return {"derived": False, "value": event.get("destination_ip"), "type": "ipaddress"}