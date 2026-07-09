def transform(event):
    protocol_map = {
        "1": "icmp",
        "6": "tcp",
        "17": "udp",
        "41": "ipv6",
        "47": "gre",
        "50": "esp",
        "51": "ah",
        "58": "icmpv6",
        "89": "ospf"
    }

    details = event.get("details", {})
    proto_number = details.get("proto")

    if proto_number is not None:
        proto_str = str(proto_number)
        if proto_str in protocol_map:
            event["network_protocol"] = protocol_map[proto_str]
        else:
            event["network_protocol"] = proto_str
    else:
        event["network_protocol"] = "unknown"

    return event