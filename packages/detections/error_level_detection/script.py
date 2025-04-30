def window():
    return None


def groupby():
    return None


def algorithm(event):
    if event.get("event_level") == "error":
        return 0.75
    
    
def context(event):
    alert_name = event.get("alert_name")
    alert_id = event.get("alert_id")
    alert_type = event.get("alert_type")
    alert_severity=event.get("alert_severity")
    alert_score=event.get("alert_score")
    context ="Recived error level event, indicating an alert named"

    if alert_name:
        context += "indicating an alert named " + alert_name
    if alert_id:
        context += " with ID " + alert_id
    if alert_type:
        context += ". The alert is categorized as " + alert_type
    if alert_score:
        context += " and  a score of "+ alert_score
    if alert_severity:
        context += " and its severity level is " + alert_severity
    return context


def criticality():
    return "HIGH"

def tactic():
    return "Command and Control(TA0011)"


def technique():
    return "Application Layer Protocol (T1071)"



def artifacts():
    try:
        return stats.collect([
            "event_category_id",
            "source_ip",
            "alert_name",
            "alert_id",
            "alert_type",
            "alert_score",
            "alert_severity",
        ])
    except Exception as e:
        raise e


def entity(event):
    ip=event.get("source_ip") if event.get("source_ip") is not None else event.get("source_remote_ip")
    return {"derived": False, "value": ip , "type": "ipaddress"}
