# Account Logon Activity:
# Track successful and failed logon attempts to the Active Directory domain.
# Example query: "EventCode:4624 OR EventCode:4625"

# this to return window (5s , 5m) for which events needs to be aggregated else return null, this has to be small window, for larger windows use scheduled detections
def window():
    return '1m'


# this should return list of attributes to group algorithm data, this should be only provided in case of window is not None
def groupby():
    return ['destination_account_name']


# this to return double value for riskscore attached to this event based on detection algo ,  aggregated will receive as events list else it will be a single event
def algorithm(event):
    id = event.get('event_id')
    err = event.get('error_message')
    if id is not None and event.get('event_id') in ["4625"] and err is not None and event.get('error_message') == "Account locked out":
        if stats.count('event_id') > 5:
            return 0.75
        return 0.0


# this to return html string to add context to detection
def context(event):
    destination_account_name = event.get("destination_account_name")
    return 'Abnormal number of login attempts made from account (' + (destination_account_name if destination_account_name else 'None') + ')'


# this to return criticality induced by this detection [LOW MEDIUM HIGH CRITICAL]
def criticality():
    return 'HIGH'


# this to return mapping with MITRE attack tactics
def tactic():
    return 'Credential Access (TA0006)'

# this to return mapping with MITRE attack technique


def technique():
    return 'Brute Force (T1110)'



def artifacts():
    try:
        return stats.collect(['event_id','destination_account_name', 'destination_account_domain', 'destination_security_id'])
    except Exception as e:
        raise e


def entity(event):
    return {'derived': False,
            'value': event.get('destination_security_id'),
            'type': 'securityid'}
