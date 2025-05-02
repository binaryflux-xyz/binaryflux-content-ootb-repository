def window():
    return "30m"


def groupby():
    return ["applicationname"]

def algorithm(event_data):

    # Check conditions for account created and deleted within a small window of time
    if "Account Create" in event_data.get("event_message")  and stats.count("applicationname"):
        return 0.0
    elif "Account Delete" in event_data.get("event_message"):
        stats.getcount("applicationname") > 1
        return 0.75
    
    return 0.0



def context(event_data):
    applicationname = event_data.get("applicationname")
    return (
        "The creation and deletion of a new account within a small window of time in system logs by the "
        +(applicationname if applicationname else 'None')
        + " application flags a concerning pattern."
    )


def criticality():
    return "HIGH"


def tactic():
    return "Initial Access(TA0001)"


def technique():
    return "Valid Accounts(T1078)"


def artifacts():
    try:
        return stats.collect(['applicationname','event_severity','process_id','facility_name'])
    except Exception as e:
        raise e
        


def entity(event):
    return {
        "derived": False,
        "value": event.get("applicationname"),
        "type": "applicationname",
    }
