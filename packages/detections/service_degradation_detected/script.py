def window():
    return None

def groupby():
    return None

def algorithm(event):
    errors = int(event.get("http_5xx", 0))
    connections = int(event.get("connection_count", 0))

    if errors > 200 and connections > 50000:
        return 1.0
    return 0.0

def context(event):
    return "This detection triggered because HTTP 5xx errors exceeded 200 while active connections exceeded 50000 on VIP=%s. Current 5xx=%s, Connections=%s. This strongly suggests service degradation caused by overload, backend instability, or capacity exhaustion." % (
        event.get("vip", "unknown"),
        event.get("http_5xx", 0),
        event.get("connection_count", 0)
    )

def criticality():
    return "CRITICAL"

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