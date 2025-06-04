"""
Instructions for Content Creators:
- Implement the required functions based on your detection algorithm and use case.
- Each function has a placeholder for customization.
"""

def window():
    """
    Returns the window duration for event aggregation. 
    Smaller windows should be defined here (e.g., 5s, 5m). For larger windows, 
    use scheduled detections.

    Returns:
        str | None: The window duration as a string (e.g., '5s', '5m') or None.
    """
    # TODO: Define your window logic (e.g., '5s' for 5 seconds, '5m' for 5 minutes)
    return None


def groupby() :
    """
    Returns a list of attributes to group events by, 
    used only if a window is defined (window() is not None).

    Returns:
        list: List of attribute names to group by.
    """
    # TODO: Define the grouping logic
    return None


def algorithm(event) :
    if event.get("event_type") == "anomaly" or event.get("event_subtype") == "anomaly":
        return event.get("alert_score") / 100
    
    return 0.0


def context(event) :
    event_severity = event.get("event_severity")
    device_name = event.get("source_device_name")
    policy_type = event.get("policy_type")
    event_level = event.get("event_level")
    event_attack = ""
    if event.get("details"):
        event_attack = event.get("details").get("event_attack")
    event_message = ""
    if event.get("event_message"):
        event_message = event.get("event_message").replace("anomaly:", "")
    return "A " + event_severity + " severity anomaly was detected by " + device_name + " using  " + policy_type + " policy. The " + event_level + " was triggered by " + event_attack + " attack, where " + event_message


def criticality():
    """
    Returns the criticality level for the detection (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL').

    Returns:
        str: Criticality level.
    """
    # TODO: Define the criticality of the detection
    return 'CRITICAL'


def tactic():
    """
    Maps the detection to a MITRE ATT&CK tactic.

    Returns:
        str: MITRE tactic.
    """
    # TODO: Map the detection to a MITRE tactic
    return "Impact (TA0040)"


def technique():
    """
    Maps the detection to a MITRE ATT&CK technique.

    Returns:
        str: MITRE technique.
    """
    # TODO: Map the detection to a MITRE technique
    return "Endpoint Denial of Service (T1499)"


def artifacts():
    try:
        return stats.collect([
            "source_ip",
            "event_message",
            "source_port",
            "destination_ip",
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
