def window():
    return None

def groupby():
    return None

def algorithm(event):
    status = event.get("health_check_status", "")
    failed = int(event.get("failed_checks", 0))

    if status == "down" and failed > 5:
        return 0.75
    return 0.0

def context(event):
    return "This detection triggered because backend server %s failed health checks and was marked down. Failed Checks=%s, VIP=%s. This may reduce available capacity and impact user traffic if redundancy is limited." % (
        event.get("backend_server", "unknown"),
        event.get("failed_checks", 0),
        event.get("vip", "unknown")
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
        "value": event.get("backend_server", "unknown"),
        "type": "ipaddress"
    }