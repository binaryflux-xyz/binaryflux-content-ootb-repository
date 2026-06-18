def window():
    return None

def groupby():
    return None

def algorithm(event):
    errors = int(event.get("http_5xx", 0))

    if errors > 200:
        return 0.75
    return 0.0

def context(event):
    return "This detection triggered because HTTP 5xx responses exceeded 200 on VIP=%s. Current 5xx Count=%s. Server-side errors usually indicate backend failures, overload, timeouts, or application instability impacting end users." % (
        event.get("vip", "unknown"),
        event.get("http_5xx", 0)
    )

def criticality():
    return "HIGH"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Service Stop (T1489)"

def entity(event):
    return {
        "derived": False,
        "value": event.get("vip"),
        "type": "ipaddress"
    }