def window():
    return None

def groupby():
    return None

def algorithm(event):
    connections = int(event.get("connection_count", 0))

    if connections > 80000:
        return 0.75
    return 0.0

def context(event):
    return "This detection triggered because active connections exceeded 80000 on VIP=%s. Current Connection Count=%s. High connection load may cause latency, connection drops, backend exhaustion, or degraded application performance." % (
        event.get("vip", "unknown"),
        event.get("connection_count", 0)
    )

def criticality():
    return "HIGH"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Resource Hijacking (T1496)"

def entity(event):
    return {
        "derived": False,
        "value": event.get("vip"),
        "type": "ipaddress"
    }