
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get("user_role") != "admin" and event.get("event_action") == "change_policy":
        return 1.0  # Unauthorized change by non-admin user
    return 0.0

def context(event_data):
   return "An unauthorized policy change was attempted by a non-admin user (" + event_data.get('user_name') + "). This action, marked as 'change_policy', was performed without the appropriate administrative privileges and requires immediate review." 


def criticality():
    return "CRITICAL"


def tactic():
    return "Privilege Escalation (TA0004)"
 

def technique():
    return "Exploitation of Vulnerability (T1068)"


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}


def artifacts():
    try:
        return stats.collect(
            [
                "applicationname",
                "source_ip",
                "user_name",
                "destination_port",
                "destination_ip",
                "source_hostname"
            ]
        )
    except Exception as e:
        raise e