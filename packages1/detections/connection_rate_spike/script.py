def window():
    return None

def groupby():
    return None

def algorithm(event):
    rate = int(event.get("new_connections_per_sec", 0))

    if rate > 10000:
        return 0.75
    return 0.0

def context(event):
    return "This detection triggered because new connection rate exceeded 10000 connections per second on VIP=%s. Current Rate=%s. Sudden spikes may indicate traffic floods, automated clients, or abnormal demand impacting service stability." % (
        event.get("vip", "unknown"),
        event.get("new_connections_per_sec", 0)
    )

def criticality():
    return "HIGH"

def tactic():
    return "Impact (TA0040)"

def technique():
    return "Network Denial of Service (T1498)"

def entity(event):
    return {
        "derived": False,
        "value": event.get("vip", "unknown"),
        "type": "ipaddress"
    }