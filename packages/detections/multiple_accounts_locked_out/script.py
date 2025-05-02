def window():
    return "5m"


def groupby():
    return ["applicationname"]

def algorithm(event):
    if (
        "Account locked out" in event.get("event_message")
        and stats.count("applicationname") > 5
    ):
        return 1.0
    return 0.0

def context(event_data):
    applicationname = event_data.get("applicationname")
    event_message = event_data.get("event_message")
    return (
        "The detection, which contains "
        + (event_message if event_message else 'None')
        + ", indicates that several user accounts within the system have been locked due to exceeding the permitted number of unsuccessful login attempts for the "
        + (applicationname if applicationname else 'None')
        + " application."
    )


def criticality():
    return "CRITICAL"


def tactic():
    return "Credential Access(TA0006)"


def technique():
    return "Brute Force(T1110)"



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
