def window():
    return None
def groupby():
    return None
  
def algorithm(event):
    # Ensure it's Event ID 4672 (Special Logon)
    if event.get('event_id') != 4672:
        return 0.0  # Ignore other events

    # Extract key fields
    user = event.get("source_account_name", "").lower()
    privileges = [priv.lower() for priv in event.get("privileges", [])]

    # List of known system accounts to ignore
    ignored_accounts = ["system", "local service", "network service", "administrator","SANAKA$"]

    # List of high-risk privileges
    critical_privileges = [
        "sedebugprivilege",
        "seimpersonateprivilege",
        "setakeownershipprivilege",
        "seloaddriverprivilege"
    ]

    # Ignore known system accounts
    if user in ignored_accounts:
        return 0.0  # Ignore system accounts

    # Only trigger if high-risk privileges are assigned
    if any(priv in privileges for priv in critical_privileges):
        return 0.5  # Fixed score for risky privilege assignments

    return 0.0  # Ignore low-risk events


  
def context(event_data):
    return "Admin privileges were assigned to user '{}' from domain '{}'.".format(
        event_data.get('source_account_name', 'Unknown'),
        event_data.get('source_account_domain', 'Unknown')
    )
def criticality():
    return 'MEDIUM'
def tactic():
    return 'Privilege Escalation (TA0004)'
def technique():
    return 'Permission Groups Modification (T1098)'
def artifacts():
    return stats.collect(['source_account_name', "event_id", "privileges"])
def entity(event):
    return {'derived': False, 'value': event['source_account_name'], 'type': 'entity'}