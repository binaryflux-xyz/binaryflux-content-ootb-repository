def window():
    return None


def groupby():
    return None


def algorithm(event_data):
    # TODO should be taken from variable
    commonAccounts = ["list of commonly used service accounts"]
    # Check conditions for service account performing an interactive logon
    if (
        event_data.get("event_id") in ["4624", "528", "540"]
        and event_data.get("logon_type") in [2, 10]
        and any(
            account in event_data.get("source_account_name").lower()
            for account in commonAccounts
        )
    ):
        return 0.50
    return 0.0


def context(event_data):
    source_account_name = event_data.get("source_account_name")
    source_account_domain =  event_data.get("source_account_domain")
    return (
        "Signifies an event where the service account "
        + (source_account_name if source_account_name else 'None')
        + " from "
        + (source_account_domain if source_account_domain else 'None')
        + ", typically used for automated processes, logs in interactively to a system."
    )

def criticality():
    return "MEDIUM"


def tactic():
    return "Defense Evasion (TA0005)"


def technique():
    return "Valid Accounts (T1078)"


def artifacts():
    try:
        return stats.collect(
            [
                "event_id",
                "source_account_name",
                "source_security_id",
                "source_account_domain",
                "server_workstation",
                "process_name",
                "source_logon_id",
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
