def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get("action", "") != "mitigated" and event.get("severity", "") == "critical":
        return 1.0
    return 0.0

def context(event):
    return "This detection triggered because a critical attack event was recorded but action status was not mitigated. Target=%s, Action=%s. This may indicate failed controls, policy gaps, or ongoing service risk." % (
        event.get("destination_ip", "unknown"),
        event.get("action", "unknown")
    )

def criticality():
    return "CRITICAL"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Service Stop (T1489)"

def entity(event):
    return {"derived": False, "value": event.get("destination_ip"), "type": "ipaddress"}