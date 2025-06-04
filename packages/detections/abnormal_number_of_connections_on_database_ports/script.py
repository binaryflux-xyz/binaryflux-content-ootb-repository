
# this to return window (5s , 5m) for which events needs to be aggregated else return null , this has to be small window , for larger windows use scheduled detections
def window():
    return "5m"

# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None
def groupby():
    return ['destination_port', 'source_ip', 'destination_ip']


# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event
def algorithm(event):
    stats_label = "db_port_detection"
    if event.get("destination_port") in [3306, 5432]:
        connection_count = stats.count(stats_label)
        if connection_count > 5:  # Threshold for abnormal number of connections
            return 0.80  # Likely DB enumeration
    return 0.0


# this to return html string to add context to detection
def context(event):
    applicationname = event.get("applicationname")
    event_message = event.get("event_message")
    return (
        ("The occurrence of a large number of connections on database ports"
        + " indicates a possible account enumeration attempt."
        + " Source IP: " + event.get("source_ip")
        + " Destination IP: " + event.get("destination_ip")
        + " Destination Port: " + str(event.get("destination_port"))
        + " Connection Count: " + str(stats.getcount("db_port_detection")))
    )


# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]
def criticality():
    return "MEDIUM"


# this to return mapping with MITRE attack tactics
def tactic():
    return "Discovery (TA0007)"


# this to return mapping with MITRE attack technique
def technique():
    return "Network Service Scanning (T1046)"


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
