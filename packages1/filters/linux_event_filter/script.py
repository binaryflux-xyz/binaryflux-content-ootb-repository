def condition(event):
    keywords = ['Account locked out','STATUS_LOGON_SUCCESS', 'STATUS_LOGON_FAILURE', 'Account Create', 'Account Delete'] 
    for keyword in keywords: 
        if keyword in event.get('message'): 
            return True 
    return False
    