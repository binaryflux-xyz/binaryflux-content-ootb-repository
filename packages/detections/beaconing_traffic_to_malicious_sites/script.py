def window():
    return None


def groupby():
    return None

def algorithm(event):

    if (
        event.get("event_category_id") is not None
        and event.get("user_name") is not None
        and event.get("user_name") not in ["UNKNOWN", "N/A"]
        and event.get("event_category_id") is not None
        and any(
            category in event.get("event_category_id")
            for category in [
                "Malicious",
                "Phishing",
                "Potential Unwanted Software",
                "Scam",
                "Suspicious",
                "ilac",
                "Browser Exploits",
                "Potential Illegal Software",
                "PUPs",
                "Spyware",
                "Computer Hacking",
                "Botnet",
                "Spam",
                "malware",
                "Unclassified",
                "128",
                "154",
                "164",
                "166",
                "167",
                "172",
                "193",
                "194",
                "200",
                "205",
                "206",
                "207",
                "213",
                "214",
                "218",
                "219",
                "220",
                "Criminal Activity",
                "Hacking",
                "Spam URLs",
                "Phishing & Fraud",
                "ilac",
            ]
        )
    ):
        return 0.75
    else:
        return 0.0


def context(event_data):
    os_name = event_data.get("os_name")
    source_ip = event_data.get("source_ip")
    network_protocol = event_data.get("network_protocol")
    destination_country = event_data.get("destination_country")
    destination_ip = event_data.get("destination_ip")
    event_duration = event_data.get("event_duration")
    network_bytes_out = event_data.get("network_bytes_out")
    network_bytes_in = event_data.get("network_bytes_in")
    network_bytes_in = event_data.get("network_bytes_in")
    applicationname = event_data.get("applicationname")
    application_category = event_data.get("application_category")
    application_risk = event_data.get("application_risk")
    policy_type = event_data.get("policy_type")
    policy_id = event_data.get("policy_id")
    return (
        "A " +( os_name if os_name else "None") + 
        " device  (IP: " + (source_ip if source_ip else "None") + 
        ") initiated a secure connection over " + (network_protocol if network_protocol else "None") +
" protocol to a destination in the " + (destination_country if destination_country else "None") + " "+
        (destination_ip if destination_ip else "None") + 
        ". The connection lasted for " + (event_duration if event_duration else "None") + 
        " seconds, with " +( network_bytes_out if network_bytes_out else "None")+ " bytes sent from the network and "+
        (network_bytes_in if network_bytes_in else "None")+ " received on newtork which have excceds the threshold of 10MB. The application identified was "+
        (applicationname if applicationname else "None") + ", categorized under "+ (application_category if application_category else "None" )+ 
        " with an " + (application_risk if application_risk else "None")+ " risk. This activity triggered a beaconing behavious  in network traffic in accordance with "+
        (policy_type if policy_type else "None") + (policy_id if policy_type else "None") + "."
        )

def criticality():
    return "HIGH"


def tactic():
    return "Command and Control(TA0011)"


def technique():
    return "Application Layer Protocol (T1071)"


def artifacts():
    try:
        return stats.collect(["event_category_id", "source_ip", "network_protocol", "applicationname","destination_country"])
    except Exception as e:
        raise e


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}
