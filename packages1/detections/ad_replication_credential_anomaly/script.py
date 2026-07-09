def window():
    return None


def groupby():
    return None


def algorithm(event_data):
    
    if (event_data.get('event_type') == 'AUDIT_FAILURE') and (event_data.get('event_id') =='4776'):
        return 0.5  
    return 0.0 


def context(event):
    source_logon_id = event.get("source_logon_id")
    source_workstation = event.get("source_workstation")
    event_id= event.get("event_id")

    if event_id == "4776":
        context ="Received audit failure error in logs every time this event generates when a credential validation occurs using NTLM authentication " + (source_logon_id if source_logon_id else "none" ) +","+ (source_workstation if source_workstation else "none" ) +","+ (event_id if event_id else "none")+"."
    return context

def criticality():
    return "MEDIUM"


def tactic():
    return "Prevent (TA0007)"


def technique():
    return "Network Segmentation and Boundary Protection (T1547)"


def artifacts():
    try:
        return stats.collect(["source_logon_id", "source_workstation","event_id"])
    except Exception as e:
        raise e


def entity(event):
    return {"derived": False, "value": event.get("source_logon_id"), "type": "logonid"}
