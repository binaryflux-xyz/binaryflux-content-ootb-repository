def window():
    return "5m"

def groupby():
    return ["source_ip"]

def algorithm(event):
    stats_label = "http_request_detection"
    if event.get("details").get("proto") == "HTTP":
        request_count = stats.count(stats_label)
        if request_count > 500:  
            return 0.95   # Unusual HTTP traffic pattern detected
    return 0.0

def context(event_data):
    return "More than 500 HTTP requests were made from the same source IP (request_count) within a short timeframe, indicating an unusual traffic pattern. This could be a sign of potential command-and-control communication or automated scanning, and warrants immediate attention."

def criticality():
    return "HIGH"


def tactic():
    return "Command and Control (TA0011)"
 

def technique():
    return "Application Layer Protocol (T1071)"


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}


def artifacts():
    try:
        return stats.collect(
            [
                "applicationname",
                "source_ip",
                "destination_port",
                "destination_ip",
                "source_hostname"
            ]
        )
    except Exception as e:
        raise e