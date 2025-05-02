def window():
    return None

def groupby():
    return None


def algorithm(event_data):

    if (event_data.get('event_id') == "4673" and ('LOCAL SYSTEM' in event_data.get('source_security_id') or  'NETWORK SERVICE'  in event_data.get('source_security_id') or  'LOCAL SERVICE'  in event_data.get('source_security_id'))):
        return 0.50
    return 0.0


def context(event_data):
    source_security_id = event_data.get("source_security_id")
    return 'Unauthorized access or activation of elevated privileges occurs by ,"'+(source_security_id if source_security_id else 'None') + '" posing risks of security breaches and misuse of system resources.'


def criticality():
    return 'MEDIUM'


def tactic():
    return 'Privilege Escalation'


def technique():
    return 'Credential Access (TA0006)'


def artifacts():
    try:
        return stats.collect(['event_id','source_account_name','source_account_domain','source_security_id','source_logon_id'])
    except Exception as e:
        raise e


def entity(event):
    return {
        'derived': False,
        'value': event.get('source_account_name'),
        'type': 'accountname'
    }
