def window():
    return None


def groupby():
    return None

def algorithm(event_data):
    
    if (event_data.get('event_type') == 'AUDIT_FAILURE') and (event_data.get('event_id') =='4769' or event_data.get('event_id') =='4771' or event_data.get('event_id')=='4768'):
        return 0.75  
    return 0.0 



def context(event):
    destination_ip = event.get("destination_ip")
    destination_port = event.get("destination_port")
    serviceinformation=event.get("serviceinformation")
    descriptions=event.get("descriptions")
    source_account_name=event.get("source_account_name")
    source_account_domain=event.get("source_account_domain")
    service_name=event.get("service_name")
    event_id=event.get("event_id")

    if event_id == "4769":
        context = "Received audit failure error in logs where the logon event happened on the accessed machine which is different from the domain controller that issued the service ticket. " + (destination_ip if destination_ip else "none" ) +" "+ ( destination_port if destination_port else "none") + " "+(serviceinformation if serviceinformation else "none") + " "+(descriptions if descriptions else "none") +" "+ (source_account_name if source_account_name else "none") + " "+(source_account_domain if source_account_domain else "none")+". "
    elif event_id == "4771":
        context="Received audit failure error in logs when the pre-authentication failed if the ticket was malformed or damaged during transit and could not be decrypted " + (destination_ip if destination_ip else "none" ) +" "+ (destination_port if destination_port else "nono") + " " +(serviceinformation if serviceinformation else "none") + " "+(descriptions if descriptions else "none") + " "+(source_account_name if source_account_name else "none") +" "+ (source_account_domain if source_account_domain else  "none")+". "
    elif event_id == "4768":
        context="Received audit failure error in logs and generates events every time when the Key Distribution Center issues a Kerberos Ticket Granting Ticket (TGT) and occurs only on domain controllers " + ( destination_ip if destination_ip else "none" ) +" "+ (destination_port if destination_port else "none" ) +" "+ (descriptions if descriptions else "none") +  " "+( service_name if service_name else "none") +"."



    return context


def criticality():
    return "HIGH"


def tactic():
    return "Credential Access (TA0006)"


def technique():
    return "Steal or Forge Kerberos Tickets (T1558.003)"


def artifacts():
    try:
        return stats.collect(["destination_ip", "destination_port","event_id","serviceinformation","source_account_name","source_account_domain","destination_ip"])
    except Exception as e:
        raise e


def entity(event):
    return {"derived": False, "value": event.get("source_account_name"), "type": "accountname"}
