def window():
    return "2m"

def groupby():
    return ["vip"]

def algorithm(event):
    # Requires platform support for min/max aggregation across grouped events
    return 0.50

def context(event):
    return "This detection triggered because backend traffic distribution appears uneven for VIP=%s within the last 2 minutes. Significant imbalance may overload some servers while others remain underutilized, increasing risk of degraded performance." % (
        event.get("vip", "unknown")
    )

def criticality():
    return "MEDIUM"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Service Stop (T1489)"

def entity(event):
    return {
        "derived": False,
        "value": event.get("vip", "unknown"),
        "type": "ipaddress"
    }