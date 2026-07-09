def condition(event):

    app = event.get('url') if event.get('url') is not None else \
            event.get('source_hostname') if event.get('source_hostname') is not None else \
            event.get('applicationname')
    
    keywords = ['tcp','udp','netbios forward','PING','UNKNOWN','SNMP',
                'POP3S','HTTP','DNS','SSL','Endpoint Control Registration',
                'Microsoft.Windows.Update']
    
    if app is None:
        return False
    if any(keyword in app for keyword in keywords):
        return False
    
    return True