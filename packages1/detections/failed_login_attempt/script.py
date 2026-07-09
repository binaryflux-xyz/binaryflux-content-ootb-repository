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
    """
    Calculates and returns a risk score based on the detection algorithm.

    Args:
        event (dict): Parsed event data.

    Returns:
        float: Calculated risk score.
    """
    # TODO: Define the risk score calculation based on event attributes
    
    if event.get('event_action') == 'login' and event.get('event_status') == 'failed' and event.get('source_ip') != '127.0.0.1':
      return 0.5
    return None


def context(event) :
    """
    Returns an  string to provide additional context to the detection.

    Args:
        event (dict): Parsed event data.

    Returns:
        str:  context string.
    """
    # TODO: Provide HTML context to explain the detection
    return event.get("details").get("message")


def criticality():
    """
    Returns the criticality level for the detection (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL').

    Returns:
        str: Criticality level.
    """
    # TODO: Define the criticality of the detection
    return 'MEDIUM'


def tactic():
    """
    Maps the detection to a MITRE ATT&CK tactic.

    Returns:
        str: MITRE tactic.
    """
    # TODO: Map the detection to a MITRE tactic
    return "Credential Access (TA0006)"


def technique():
    """
    Maps the detection to a MITRE ATT&CK technique.

    Returns:
        str: MITRE technique.
    """
    # TODO: Map the detection to a MITRE technique
    return "Brute Force (T1110)"


def artifacts():
    """
    Extracts the artifacts required to be saved as part of this detection.

    Returns:
        list: List of artifacts to be collected.
    """
    # TODO: Define the artifacts to be extracted and saved
    return stats.collect(['source_device_id','source_device_name','source_ip',])

def entity(event):
    """
    Defines the entity derived from the event (e.g., employee, system, IP address).

    Args:
        event (dict): Parsed event data.

    Returns:
        dict: The derived entity with type and value.
    """
    # TODO: Derive the entity from the event, or leave as is if no derivation is required
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
    # Example: return {'derived': True, 'from': {'type': 'email', 'value': event['actor'], 'class': 'identity'}, 'type': 'employee'}
