def window():
    return "10m"

def groupby():
    return ["source_ip"]

def algorithm(event):
    stats_label = "src_ip_alert_detection"
    if event.get("event_action") == "alert":
        alert_count = stats.count(stats_label)
        if alert_count > 100:  # More than 100 alerts from the same source in 10 minutes
            return 0.90  # High rate of alerts from source IP
    return 0.0

def context(event_data):
    return "More than 100 alerts were triggered from the same source IP (" + event_data.get('source_ip') + ") within a 10-minute window. This high frequency of alerts may indicate suspicious scanning activity or brute-force attempts, requiring further investigation to identify potential threats."


def criticality():
    return "HIGH"


def tactic():
    return "Discovery (TA0007)"
 

def technique():
    return "Network Service Scanning (T1046)"


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}


def artifacts():
    try:
        return stats.collect(
            [
                "applicationname",
                "source_ip",
                "destination_port",
                "event_category_desc",
                "destination_ip",
                "source_hostname"
            ]
        )
    except Exception as e:
        raise e