def window():
    return None


def groupby():
    return None

def algorithm(event_data):
    
    if (event_data.get('event_type') == 'AUDIT_FAILURE') and (event_data.get('event_id') =='4656' or event_data.get('event_id') =='4674'):
        return 0.75  
    return 0.0 


def context(event):
    service_name = event.get("service_name")
    service_type = event.get("service_type")
    server=event.get("server")
    source_account_domain=event.get("source_account_domain")
    source_account_name=event.get("source_account_name")
    process_name=event.get("process_name")
    process_id=event.get("process_id")
    access=event.get("access")
    event_id=event.get("event_id")

    if event_id == "4656":
        context = "Received audit failure error in logs and generates event if the objects SACL has the required ACE to handle the use of specific access rights." + ( service_name if service_name else "none" ) + (service_type if service_type else "none" ) +" "+ (server if server else "none") +" "+  ( source_account_domain if source_account_domain else "none") + " "+ (source_account_name if source_account_name else "none") + " "+ (process_name if process_name else "none")  +" "+ ( process_id if process_id else "none" ) + " "+(access if access else "none")+"."
    elif event_id == "4674":
        context="Received audit failure error in logs and events generates when an attempt to perform privileged operations on a protected subsystem object fails after the object is already opened. The details include: "  + ( source_account_name if source_account_name else "none" ) + " "+ (source_account_domain if source_account_domain else "none") +" "+ (server if server else "none") + " "+ (service_name if service_name else "none") + " "+(service_type if service_type else "none") +" "+ (process_id if process_id else "none") + " "+ (process_name if process_name else "none") +" "+ (access if access else "none")+"."


    return context


def criticality():

    return "HIGH"


def tactic():
    return "Defense Evasion (TA0005)"


def technique():
    return "Disabling Security Tools (T1089)"


def artifacts():
    try:
        return stats.collect(["service_name", "service_type","event_id","source_account_domain","source_account_name","process_name","process_id",])
    except Exception as e:
        raise e


def entity(event):
    return {"derived": False, "value": event.get("source_account_name"), "type": "accountname"}
