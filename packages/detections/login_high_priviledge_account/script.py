def window():
    return None
    
def groupby():
    return None
    
    
def algorithm(event_data):
    
    # Check conditions for explicit login to high privileged account
    if (event_data.get('event_id') == "4648" and
        '$' not in event_data.get('source_account_name')):
        return 0.50  
    return 0.0  
        

def context(event_data):
    destination_account_name=event_data.get('destination_account_name')
    destination_account_domain=event_data.get('destination_account_domain')
    source_account_name=event_data.get('source_account_name')
    source_account_domain=event_data.get('source_account_domain')
    destination_server_name=event_data.get('destination_server_name')
    return "Explicit login to high privileged account detected. Source account: "+( source_account_name if source_account_name else 'unknown')+" from "+ (source_account_domain if source_account_domain else 'unknown domain')+". Destination account: "+( destination_account_name if destination_account_name else 'unknown')+" from " +(destination_account_domain if destination_account_domain else 'unknown domain')+". Destination server: "+ (destination_server_name if destination_server_name else 'unknown')+"."

def criticality():
    return 'MEDIUM'
    
def tactic():
    return 'Defense Evasion (TA0005)'
    
def technique():
    return 'Valid Accounts (T1078)'
    

def artifacts():
    try:
        return stats.collect(['event_id','source_account_name','source_security_id','source_account_domain','destination_account_name','destination_account_domain','source_logon_guid','destination_server_name'])
    except Exception as e:
        raise e
    
def entity(event):
    return {'derived': False,
            'value': event.get('source_account_name'),
            'type': 'accountname'}