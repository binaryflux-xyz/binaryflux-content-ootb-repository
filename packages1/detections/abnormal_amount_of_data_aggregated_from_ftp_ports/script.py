
def window():
    return None

def groupby():
    return None

def algorithm(event):
    if event.get("destination_port") != "21":
        return 0.0

    sentbytes = (
        int(event.get("network_bytes_out"))
        if event.get("network_bytes_out") is not None
        else 0
    )

    threshold = 10000000 # to be taken from variable
    return 0.75 if sentbytes >= threshold else 0.0




def context(event_data):
    os_name = event_data.get("os_name")
    source_ip = event_data.get("source_ip")
    network_protocol = event_data.get("network_protocol")
    destination_country = event_data.get("destination_country")
    destination_ip = event_data.get("destination_ip")
    event_duration = event_data.get("event_duration")
    network_bytes_out = event_data.get("network_bytes_out")
    applicationname = event_data.get("applicationname")
    application_category = event_data.get("application_category")
    application_risk = event_data.get("application_risk")
    policy_type = event_data.get("policy_type")
    policy_id = event_data.get("policy_id")
    context = "A "

    if os_name:
        context += os_name + " device "
    if source_ip:
        context += "(IP: " + source_ip + ") "
    context += "initiated a secure connection over "

    if network_protocol:
        context += network_protocol + " protocol to a destination in "
    if destination_country:
        context += destination_country + " (IP: "
    if destination_ip:
        context += destination_ip + "). "

    if event_duration:
        context += "The connection lasted for " + str(event_duration) + " seconds. "
    if network_bytes_out:
        context += "During the connection " + str(network_bytes_out) + " bytes sent from the network and "

    if applicationname:
        context += "The identified application was " + applicationname + ", "
    if application_category:
        context += "categorized under " + application_category + ", "
    if application_risk:
        context += "with a risk level of " + application_risk + ". "

    context += "This activity triggered a detection log, indicating an abnormal amount of data transmitted over FTP port, in accordance with "

    if policy_id:
        context += " policy ID " + policy_id + "."
    return context

def criticality():
    return "HIGH"


def tactic():
    return "Exfiltration (TA0010)"


def technique():
    return "Exfiltration Over Alternative Protocol (T1048)"


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}


def artifacts():
    try:
        return stats.collect(
            [
                "source_ip",
                "network_protocol",
                "network_bytes_out",
                "destination_port",
                "policy_type",
                "application_risk",
                "destination_ip",
                "destination_country"
            ]
        )
    except Exception as e:
        raise e
