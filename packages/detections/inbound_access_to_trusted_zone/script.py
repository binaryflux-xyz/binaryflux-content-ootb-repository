

def window():
    return None  # No windowing needed for one-off detection

def groupby():
    return None

def algorithm(event):
    if (event.get('source_zone') == 'UNTRUST' and
        event.get('destination_zone') == 'TRUST' and
        event.get('event_action') == 'allow'
        ):
            return 0.75  # High risk score
    else:
        return 0.0  # No risk otherwise

def context(event):
    return (
        "An inbound network connection was allowed from the UNTRUST zone to the TRUST zone. "
        + "The source IP " + event.get("source_ip", "N/A") + " initiated the connection targeting the destination IP "
        + event.get("destination_ip", "N/A") + " on port " + event.get("destination_port", "N/A") + ". "
        + "The connection used the application protocol: " + event.get("network_protocol", "N/A") + ". "
        + "This may indicate potential exposure of internal assets to untrusted sources and should be reviewed."
    )


def criticality():
    return 'HIGH'

def tactic():
    return 'Initial Access (TA0001)'

def technique():
    return 'Application Layer Protocol (T1071)'

def artifacts():
    return stats.collect(['source_ip', 'destination_ip', 'destination_port', 'application', 'event_action'])

def entity(event):
    return {'derived': False, 'value': event.get('source_ip'), 'type': 'ipaddress'}
