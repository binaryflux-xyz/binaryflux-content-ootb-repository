def window():
    return None

def groupby():
    return None

def algorithm(event):
    errors = int(event.get("http_4xx", 0))

    if errors > 1000:
        return 0.50
    return 0.0

def context(event):
    return "This detection triggered because HTTP 4xx responses exceeded 1000 on VIP=%s. Current 4xx Count=%s. High client-side errors may indicate bot traffic, bad requests, authentication problems, or broken client integrations." % (
        event.get("vip", "unknown"),
        event.get("http_4xx", 0)
    )

def criticality():
    return "MEDIUM"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Valid Accounts (T1078)"

def entity(event):
    return {
        "derived": False,
        "value": event.get("vip", "unknown"),
        "type": "ipaddress"
    }