def window():
    return None
    
def groupby():
    return None
    
def algorithm(event_data):
    
    standard_folders = ['System32', 'Program Files']
    restricted_folder = 'Temporary Internet Files'
    
    process_name = event_data.get('process_name') 
    
    if event_data.get('event_id') == "4673" and not (any (folder in process_name for folder in standard_folders) or restricted_folder in process_name):
        return 0.25  # Process Name is not in standard folders or is in a restricted folder and Event ID matches
    else:
        return 0.0

 
def context(event_data):
    process_name = event_data.get("process_name")
    return 'This event generates when Process name:("'+ (process_name if process_name else 'None')+ '") runs from a non-standard or restricted folder("Temporary Internet Files"), indicating possible unauthorized or malicious activity.'

def criticality():
    return 'LOW'
    
def tactic():
    return 'Execution (TA00002)'
    
def technique():
    return 'Command and Scripting Interpreter (T1059)'
    

def artifacts():
    try:
        return stats.collect(['event_id','source_security_id','source_logon_id','source_account_domain'])
    except Exception as e:
        raise e
    
def entity(event):
    return {
        'derived': False,
        'value': event.get('process_name'),
        'type': 'process'
    }
