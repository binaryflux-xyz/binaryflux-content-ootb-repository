# condition
# d5 account_name matches with DC\d+\$ and
# user account_controller contain 'Server Trust Account' – Enabled
# 4720,  or 4738
import re


def window():
    return None


def groupby():
    return None


def algorithm(event_data):
    # Check if account_name matches the pattern 'DC\d+\$' and user account_controller contains 'Server Trust Account - Enabled'
    if event_data.get('destination_account_name') is not None and not re.match(r'DC\d+\$', event_data.get('destination_account_name')) and \
       event_data.get('user_account_control') is not None and 'Server Trust Account - Enabled' in event_data.get('user_account_control') and \
       event_data.get('event_id') is not None and event_data.get('event_id') in ["4720", "4738"]:
        return 0.50
    return 0.0


def context(event_data):
    destination_account_name=event_data.get('destination_account_name')
    destination_account_domain=event_data.get('destination_account_domain')
    source_account_name=event_data.get('source_account_name')
    source_account_domain=event_data.get('source_account_domain')
    source_info = "Source account: "+(source_account_name if source_account_name else 'unknown')+" from "+ (source_account_domain if source_account_domain else 'unknown domain')+"."
    destination_info = "Destination account: "+ (destination_account_name if destination_account_name else 'unknown') +" from "+(destination_account_domain if destination_account_domain else 'unknown domain')+"."
    return "Detected an attempt to enable 'Should never be enabled' for user accounts. This configuration should only be applied to domain controller (computer) accounts."+ (source_info  if source_info else 'None')+" "+ (destination_info  if destination_info else 'None')+"."
  

def criticality():
    return 'MEDIUM'

# this to return mapping with MITRE attack tactics


def tactic():
    return 'Defense Evasion (TA0005)'


def technique():
    return 'Account Manipulation (T1098)'


def artifacts():
    try:
        return stats.collect(['event_id','destination_account_name', 'destination_account_domain','source_account_name','source_account_domain'])
    except Exception as e:
        raise e


def entity(event):
    return {'derived': False,
            'value': event.get('source_account_name'),
            'type': 'accountname'}
