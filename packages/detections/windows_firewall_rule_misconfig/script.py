def window():
    return None


def groupby():
    return None

def algorithm(event_data):
    
    if (event_data.get('event_type') == 'AUDIT_FAILURE') and (event_data.get('event_id') =='4957' or event_data.get('event_id') =='4953'):
        return 0.5  
    return 0.0 


def context(event):
    rule_id = event.get("rule_id")
    rule_name = event.get("rule_name")
    error_message = event.get("error_message")
    event_id=event.get("event_id")

    if event_id == "4957":
        context = "Received audit failure error in logs where Windows Firewall did not apply the rule which has a rule id " +( rule_id if rule_id else 'None') +" rule name "+ (rule_name if rule_name else "none") +" with error message "+( error_message if error_message  else "None")+"."
    elif event_id == "4953":
        context="Received audit failure error in logs if Windows Firewall can't parse a rule due to a corrupted registry entry " + ( rule_id if rule_id else "none" ) +" rule name "+ (rule_name if rule_name else "none" ) + " with error message "+(error_message if error_message else "None")+"."

    return context


def criticality():

    return "MEDIUM"


def tactic():
    return "Defense Evasion  (TA0005)"


def technique():
    return "Impair Defenses: Disable or Modify System Firewall (T1562.004)"


def artifacts():
    try:
        return stats.collect(["rule_id", "rule_name","event_id"])
    except Exception as e:
        raise e


def entity(event):
    return {"derived": False, "value": event.get("rule_id"), "type": "ruleid"}
