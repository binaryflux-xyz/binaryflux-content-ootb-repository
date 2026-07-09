def window():
    return '30m'
def groupby():
    return ['destination_account_name']
def algorithm(event):
    if event['event_id'] == 4624 and int(event['logon_type']) in [2, 3, 10]:

        sourceipsdict = stats.collect(['source_ip'])
        unique_ips=len(sourceipsdict.get("source_ip"))
        if unique_ips > 5:
            return 0.5
    return 0.0
def context(event_data):
    return "User " + event_data['destination_account_name'] + " logged in from multiple unique IPs within a short time."
def criticality():
    return 'MEDIUM'
def tactic():
    return 'Credential Access (TA0006)'
def technique():
    return 'Valid Accounts (T1078)'
def artifacts():
    return stats.collect(['destination_account_name', 'source_ip', 'event_id', 'logon_type'])
def entity(event):
    return {'derived': False, 'value': event['destination_account_name'], 'type': 'entity'}