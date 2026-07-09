def window():
    return None
    
def groupby():
    return None
    
def algorithm(event_data):
    
    # Check conditions for rare audit log clearing on host
    if ("1102" in event_data.get('event_id') or "517" in event_data.get('event_id')) :
        return 0.75  
    return 0.0  
        

def context(event_data):
    source_account_name = event_data.get('source_account_name')
    source_account_domain = event_data.get('source_account_domain')
    return "Windows Security audit log was cleared by "+(source_account_name if source_account_name else 'an unknown account')+" from "+ (source_account_domain if source_account_domain else 'an unknown domain')+"."

    
    
def criticality():
    return 'MEDIUM'
    
def tactic():
    return 'Defense Evasion (TA0005)'
    
def technique():
    return 'Clear Windows Event Logs (T1070)'


def artifacts():
    try:
        return stats.collect(['event_id','source_account_name','source_account_domain','source_security_id','source_logon_id'])
    except Exception as e:
        raise e
    
def entity(event):
    return {'derived': False,
            'value': event.get('source_account_name'),
            'type': 'accountname'}