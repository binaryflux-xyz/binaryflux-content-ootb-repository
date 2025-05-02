#d1) “CN=AdminSDHolder,CN=System,DC=domain,DC=com”
#d2) class=domainDNS    
#d3) LDAP Display Name=user   
#d4) Operation\Type = Value Added or Value Deleted

def window():
    return None
    
def groupby():
    return None
    
    
def algorithm(event_data):
    # Check if "object_dn" key exists in event_data
    object_dn_value = event_data.get("object_dn", None)
    if object_dn_value is None:
        return 0.0
  
    object_dn_components = object_dn_value.split(',')
    substring = "CN=AdminSDHolder,CN=System,DC=domain,DC=com"

    # Creating a dictionary to store the key-value pairs of each component
    object_dn_dict = {}
    for component in object_dn_components:
        key, value = component.split('=')
        object_dn_dict[key] = value

    # Splitting the substring into its components and comparing with the object DN components
    substring_components = substring.split(',')
    substring_dict = {}
    for component in substring_components:
        key, value = component.split('=')
        substring_dict[key] = value

    return 0.50 if (event_data.get('event_id') in ["5136"] and \
                    all(key in object_dn_dict and object_dn_dict[key] == value for key, value in substring_dict.items()) and 
                    event_data.get('object_class') == 'domainDNS' and 
                    (event_data.get('operation_type') == 'Value Added' or event_data.get('operation_type') == 'Value Deleted')) \
                else 0.0

def context(event_data):
    service_name=event_data.get("service_name")
    service_type=event_data.get("service_type")
    object_dn=event_data.get("object_dn")
    object_guid=event_data.get("object_guid")
    object_class=event_data.get("object_class")
    operation_type=event_data.get("operation_type")
    source_account_name=event_data.get('source_account_name')
    source_account_domain=event_data.get('source_account_domain')
    return "This log captures the modification of an Active Directory object. The service "+ (service_name if service_name else 'Unknown')+" with type "+ (service_type if service_type else 'Unknown')+" modified the object identified by its distinguished name "+ (object_dn if object_dn else 'Unknown') +" and "+ (object_guid if object_guid else 'Unknown')+". The object belongs to class "+ (object_class if object_class else 'Unknown')+" and the operation type was "+( operation_type if operation_type else 'Unknown')+". The modification was performed by the account "+ (source_account_name if source_account_name else 'Unknown')+" in the domain "+ (source_account_domain if source_account_domain else 'Unknown')+"."
    
    
def criticality():
    return 'MEDIUM'
    
# this to return mapping with MITRE attack tactics
def tactic():
    return 'Defense Evasion (TA0005)'


# this to return mapping with MITRE attack technique
def technique():
    return 'File and Directory Permissions Modification (T1222)'
    

def artifacts():
    try:
        return stats.collect(['event_id','object_dn','object_guid','object_class','source_account_name','operation_type','service_name','service_type','source_account_domain'])
    except Exception as e:
        raise e
    
def entity(event):
    return {'derived': False,
            'value': event.get('source_account_name'),
            'type': 'accountname'}