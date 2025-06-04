def window():
    return "5m"

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None
def groupby():
    return ['applicationname', 'source_ip', 'destination_ip']


# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event
def algorithm(event):
    stats_label = "_deny"
    if stats_label in event.get("event_action") and stats.count(stats_label):
        return 0.0
    elif stats_label not in event.get("event_action") and stats.getcount(stats_label) > 3:
        return 0.75

    return 0.0


# this to return html string to add context to detection
def context(event):
    applicationname = event.get("applicationname")
    event_message = event.get("event_message")
    return (
        ("The occurrence of a brute force attack followed by a successful login using internal credentials for the "
        + applicationname if applicationname else '')
        + " application highlights a significant security threat with message : "
        + (event_message if event_message else 'None')
        + ". Where source ip is " + event.get("source_ip") + " and destination ip is " + event.get("destination_ip")
    )


# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]
def criticality():
    return "MEDIUM"


# this to return mapping with MITRE attack tactics
def tactic():
    return "Credential Access (TA0006)"


# this to return mapping with MITRE attack technique
def technique():
    return "Brute Force (T1110)"


def artifacts():
    try:
        return stats.collect([
            "applicationname",
            "event_severity",
            "source_ip",
            "destination_ip",
            "source_port",
            "destination_port"
        ])
    except Exception as e:
        raise e
        

def entity(event):
    return {
        "derived": False,
        "value": event.get("source_ip"),
        "type": "ipaddress",
    }