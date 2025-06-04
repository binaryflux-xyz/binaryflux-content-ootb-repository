def window():
    return None


def groupby():
    return None

def algorithm(event):
    destination_ip = event.get("destination_ip")
    destination_ports = ["23", "22", "3389"]
    application_protocols = ["ICMP", "TELNET", "ssh", "RDP"]
    account_name = event.get("user_name")

    sentbytes = (
        int(event.get("network_bytes_out"))
        if event.get("network_bytes_out") is not None
        else 0
    )
    receivedbytes = (
        int(event.get("network_bytes_in"))
        if event.get("network_bytes_in") is not None
        else 0
    )

    account_name = event.get("user_name")

    condition1 = event.get("destination_port") == "53" or (
        event.get("network_protocol") is not None
        and ("HTTP" in event.get("network_protocol") or "HTTPS" in event.get("network_protocol"))
    )


    bytesTransferred = sentbytes + receivedbytes
    threshold = 10000000 # to be taken from variable

    condition2 = (
        event.get("destination_port") in destination_ports
        or event.get("network_protocol") in application_protocols
    ) and (
        account_name is not None
        and account_name not in ["-", "UNKNOWN", ""]
        and "$" not in account_name
    )

    final_condition = condition1  or condition2

    blocked_ranges = [
        "10.100.11.64/27",
        "10.100.11.96/27",
        "10.100.11.128/26",
        "10.100.11.192/27",
        "10.100.11.224/27",
        "10.100.12.0/24",
        "10.100.13.0/24",
        "10.100.14.0/24"
    ]
    in_blocked_range = any(range.inCIDRRange(destination_ip, cidr) for cidr in blocked_ranges)

    if final_condition and not in_blocked_range and bytes_transferred >= threshold:
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
        context += destination_ip + "), which is outside the range of the organization's CIDR. "

    if event_duration:
        context += "The connection lasted for " + str(event_duration) + " seconds. "
    if network_bytes_out:
        context += "During the connection " + str(network_bytes_out) + " bytes sent from the network and "
    if network_bytes_in:
        context += str(network_bytes_in) + " bytes received on the network, which exceeds the threshold of 10MB. "

    if applicationname:
        context += "The identified application was " + applicationname + ", "
    if application_category:
        context += "categorized under " + application_category + ", "
    if application_risk:
        context += "with a risk level of " + application_risk + ". "

    context += "This activity triggered a detection log, indicating an abnormal amount of data transmitted over outside the defined CIDR range, in accordance with "

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
                "network_bytes_in",
                "destination_port",
                "policy_type",
                "application_risk",
                "destination_ip",
                "destination_country"
            ]
        )
    except Exception as e:
        raise e