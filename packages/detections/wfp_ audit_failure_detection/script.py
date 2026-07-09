def window():
    return None


def groupby():
    return None

def algorithm(event_data):
    
    if (event_data.get('event_type') == 'AUDIT_FAILURE') and (event_data.get('event_id') =='5152' or event_data.get('event_id') =='5157'):
        return 0.5  
    return 0.0 


def context(event):
    source_ip = event.get("source_ip")
    source_port = event.get("source_port")
    destination_ip = event.get("destination_ip")
    destination_port = event.get("destination_port")
    layer_name = event.get("layer_name")
    event_id=event.get("event_id")
    applicationname = event.get("applicationname")
    network_protocol=event.get("network_protocol")

    if event_id == "5152":
        context = "Received audit failure error in logs where Windows Filtering Platform has blocked a packet which has source ip " + (source_ip if source_ip else "none") + " source port "  + (source_port if source_port else "none" ) + " destination ip " + (destination_ip if destination_ip else "none") + " destination port " + (destination_port if destination_port else "none" ) + " layer name " + (layer_name if layer_name else "none")+"."
    elif event_id == "5157":
        context="Received audit failure error in logs and events generates when Windows Filtering Platform has blocked a connection."+ ( applicationname if applicationname else "none" ) +" "+ (source_ip if source_ip else "none" ) +" "+ (source_port if source_port else "none") + " "+ ( destination_ip if destination_ip else "none") + " "+(destination_port if destination_port else "none") + " "+(network_protocol if network_protocol else "none") + " "+(layer_name if layer_name else "none")+"."

    return context

def criticality():
    return "MEDIUM"


def tactic():
    return "Prevent (TA0007)"


def technique():
    return "Network Segmentation and Boundary Protection (T1547)"


def artifacts():
    try:
        return stats.collect(["source_ip", "source_port","event_id","destination_ip","destination_port"])
    except Exception as e:
        raise e


def entity(event):
    return {"derived": False, "value": event.get("source_ip"), "type": "ipaddress"}
