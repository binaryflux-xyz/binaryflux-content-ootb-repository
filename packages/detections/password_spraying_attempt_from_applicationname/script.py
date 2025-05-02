def window():
    return "5m"


def groupby():
    return ["applicationname"]

def algorithm(event):
    if (
        "STATUS_LOGON_FAILURE" in event.get("event_message")
        and stats.count("applicationname") > 5
    ):
        return 0.50
    return 0.0


def context(event_data):
    applicationname = event_data.get("applicationname")
    event_message = event_data.get("event_message")
    return (
        ("The event involving repeated login attempts with varying passwords for the "
        + applicationname if applicationname else '')
        + " application raises concerns, as it poses a risk of unauthorized system access: "
        +( event_message if event_message else 'None')
        + "."
    )

def criticality():
    return "MEDIUM"


def tactic():
    return "Credential Access(TA0006)"


def technique():
    return "Password Spraying(T1110.003)"


def artifacts():
    try:
        return stats.collect([
            "applicationname",
            "event_severity",
            "source_hostname",
            "process_id",
            "structured_data",
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
