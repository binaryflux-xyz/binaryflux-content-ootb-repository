# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
    return "5m"

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None
def groupby():
    return ["applicationname"]


# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event
def algorithm(event):
    if "STATUS_LOGON_FAILURE" in event.get("event_message") and stats.count(
        "applicationname"
    ):
        return 0.0
    elif "STATUS_LOGON_SUCCESS" in event.get("event_message"):
        stats.getcount("applicationname") > 3
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
        + "."
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
            "source_hostname",
            "process_id",
            "facility_name",
        ])
    except Exception as e:
        raise e
        

def entity(event):
    return {
        "derived": False,
        "value": event.get("applicationname"),
        "type": "applicationname",
    }
