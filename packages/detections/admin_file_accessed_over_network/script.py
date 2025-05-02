def window():
    return None

def groupby():
    return None


def algorithm(event_data):
    # Check if "filename" key exists and its value is not None
    if "filename" in event_data and event_data.get("filename") is not None:
        # Check conditions for admin share enumeration
        if (event_data.get("event_id") in ["5140", "5145"]) and (
            "admin$" in event_data.get("filename").lower()
            or "c$" in event_data.get("filename").lower()
            or "ipc$" in event_data.get("filename").lower()
        ):
            return 0.50
    return 0.0


def context(event_data):
    source_account_name = event_data.get("source_account_name")
    source_account_domain = event_data.get("source_account_domain")
    source_ip = event_data.get("source_ip")
    source_port = event_data.get("source_port")
    io_type_name = event_data.get("io_type_name")
    io_type_path = event_data.get("io_type_path")
    io_type_relative_destination_path = event_data.get(
        "io_type_relative_destination_path"
    )

    return (
        "An attempt to enumerate administrative shares on a network device was flagged. Originating from IP "
        + (source_ip if source_ip else "None")
        + " on port "
        + (source_port if source_port else "None")
        + " , the source account "
        + (source_account_name if source_account_name else "None")
        + " from "
        + (source_account_domain if source_account_domain else "None")
        + " initiated IO operation "
        + (io_type_name if io_type_name else "None")
        + " along path "
        + (io_type_path if io_type_path else "None")
        + ", targeting "
        + (io_type_relative_destination_path if io_type_relative_destination_path else "None")
        + "."
    )


def criticality():
    return "MEDIUM"


def tactic():
    return "Discovery(TA0007)"


def technique():
    return "Network Share Discovery(T1135)"


def artifacts():
    try:
        return stats.collect(
            [
                "source_account_name",
                "source_account_domain",
                "source_security_id",
                "source_logon_id",
                "service_address",
                "service_port",
                "io_type_path",
                "event_id",
            ]
        )
    except Exception as e:
        raise e


def entity(event):
    return {
        "derived": False,
        "value": event.get("source_account_name"),
        "type": "accountname",
    }
