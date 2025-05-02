#this detection for new stream (AD CRITICAL EVENT MONITORING)
def window():
    return None
    
def groupby():
    return None
    
def algorithm(event_data):
    
    if (event_data.get('event_type') == 'AUDIT_FAILURE'):
        return 0.75  
    return 0.0  



def context(event_data):
    rule_id = event_data.get("rule_id")
    rule_name = event_data.get("rule_name")
    error_message = event_data.get("error_message")
    event_id=event_data.get("event_id")
    destination_account_name=event_data.get("destination_account_name")
    destination_account_domain=event_data.get("destination_account_domain")
    host=event_data.get("host")
    event_type=event_data.get("event_type")
    source_account_name=event_data.get("source_account_name")
    source_account_domain=event_data.get("source_account_domain")
    source_security_id=event_data.get("source_security")
    source_logon_id=event_data.get("source_logon_id")
    source_logon_guid=event_data.get("source_logon_guid")
    source_ip=event_data.get("source_ip")
    source_port=event_data.get("source_port")
    user_account_control=event_data.get("user_account_control")
    ldap_display_name=event_data.get("ldap_display_name")
    operation_type=event_data.get("operation_type")
    source_workstation=event_data.get("source_workstation")
    applicationname=event_data.get("applicationname")
    destination_security_id=event_data.get("destination_security_id")
    destination_logon_id=event_data.get("destination_logon_id")
    destination_logon_guid=event_data.get("destination_logon_guid")
    destination_server_name=event_data.get("destination_server_name")
    destination_ip=event_data.get("destination_ip")
    network_protocol=event_data.get("network_protocol")
    process_command_line=event_data.get("process_command_line")
    process_id=event_data.get("process_id")
    creator_process_id=event_data.get("creator_process_id")
    creator_process_name=event_data.get("creator_process_name")
    server=event_data.get("server")
    service_address=event_data.get("service_address")
    service_port=event_data.get("service_port")
    server_workstation=event_data.get("server_workstation")
    process_io_type=event_data.get("process_io_type")
    service_name=event_data.get("service_name")
    service_type=event_data.get("service_type")
    object_dn=event_data.get("object_dn")
    object_guid=event_data.get("object_guid")
    object_class=event_data.get("object_class")
    io_type_name=event_data.get("io_type_name")
    io_type_path=event_data.get("io_type_path")
    io_type_relative_destination_path=event_data.get("io_type_relative_destination_path")
    logon_type=event_data.get("logon_type")
    layer_name=event_data.get("layer_name")
    descriptions=event_data.get("descriptions")
    access=event_data.get("access")

        # Build the context string
   

    # event_id the rule that triggered the event
    if event_id or event_type:
        context = "A security event was detected having  "
        if event_id:
            context += " event id " + str(event_id) + ". "
        if event_id:
            context += " and event type " + str(event_type) + ". "



    if rule_id or rule_name:
        context += "The event was triggered by a firewall rule "
        if rule_id:
            context += " with rule id  " + str(rule_id)
        if rule_name:
            context += " and name " + str(rule_name)
        context += ". "

    # Add the error message if present
    if error_message:
        context += "An error occurred: " + str(error_message) + ". "

    # Detail the event attributes
 
    if host:
        context += "Host: " + str(host) + ". "

    # Source details
    if source_account_name or source_account_domain or source_security_id:
        context += "Source details: "
        if source_account_name:
            context += "Account Name: " + str(source_account_name) + ", "
        if source_account_domain:
            context += "Account Domain: " + str(source_account_domain) + ", "
        if source_security_id:
            context += "Security ID: " + str(source_security_id) + ". "
    
    # Source logon details
    if source_logon_id or source_logon_guid:
        context += "Logon details: "
        if source_logon_id:
            context += "Logon ID: " + str(source_logon_id) + ", "
        if source_logon_guid:
            context += "Logon GUID: " + str(source_logon_guid) + ". "
        if source_workstation:
            context += "Source Workstation: " + str(source_logon_guid) + ". "

    
    # Source network details
    if source_ip or source_port:
        context += "Source network: "
        if source_ip:
            context += "IP: " + str(source_ip) + ", "
        if source_port:
            context += "Port: " + str(source_port) + ". "
        

    # Destination details
    if destination_account_name or destination_account_domain or destination_security_id:
        context += "Destination details: "
        if destination_account_name:
            context += "Account Name: " + str(destination_account_name) + ", "
        if destination_account_domain:
            context += "Account Domain: " + str(destination_account_domain) + ", "
        if destination_security_id:
            context += "Security ID: " + str(destination_security_id) + ". "
    
    # Destination logon details
    if destination_logon_id or destination_logon_guid:
        context += "Destination logon details: "
        if destination_logon_id:
            context += "Logon ID: " + str(destination_logon_id) + ", "
        if destination_logon_guid:
            context += "Logon GUID: " + str(destination_logon_guid) + ". "
    
    # Destination network details
    if destination_ip:
        context += "Destination IP: " + str(destination_ip) + ". "
    if destination_server_name:
        context += "Server Name: " + str(destination_server_name) + ". "

    # Other attributes
    if network_protocol:
        context += "Network Protocol: " + str(network_protocol) + ". "
    if process_command_line:
        context += "Process Command Line: " + str(process_command_line) + ". "
    if process_id:
        context += "Process ID: " + str(process_id) + ". "
    if creator_process_id:
        context += "Creator Process ID: " + str(creator_process_id) + ". "
    if creator_process_name:
        context += "Creator Process Name: " + str(creator_process_name) + ". "
    if service_name:
        context += "Service Name: " + str(service_name) + ". "
    if service_type:
        context += "Service Type: " + str(service_type) + ". "
    if object_dn:
        context += "Object DN: " + str(object_dn) + ". "
    if object_guid:
        context += "Object GUID: " + str(object_guid) + ". "
    if object_class:
        context += "Object Class: " + str(object_class) + ". "
    if applicationname:
        context += "Application Name: " + str(applicationname) + ". "


    # Additional information
    if logon_type:
        context += "Logon Type: " + str(logon_type) + ". "
    if layer_name:
        context += "Layer Name: " + str(layer_name) + ". "
    if descriptions:
        context += "Descriptions: " + str(descriptions) + ". "
    if access:
        context += "Access: " + str(access) + ". "

    if io_type_name or io_type_path or io_type_relative_destination_path:
        context += "Input Output details included "
        if io_type_name:
            context +=str(io_type_name)+ " as I/O type "
        if io_type_path:
            context += " with path " + str(io_type_path) 
        if io_type_relative_destination_path:
            context += " and relative destination path " + str(io_type_relative_destination_path) + ". "

    if server or service_address or service_port or server_workstation or process_io_type:
        context += "Server details included "
        if server:
            context +=str(server)+ "as server "
        if io_type_path:
            context +=  str(io_type_path) +" as service address "
        if service_port:
            context +=  str(service_port) +" as port "
        if server_workstation:
            context +=  str(server_workstation) +" as server workstation"
        if process_io_type:
            context +=  str(process_io_type) +" as process I/O type "
    return context

    
    
    
    
    
def criticality():
    return 'HIGH'
    
def tactic():
    return 'Credential Access (TA0006)'
    
def technique():
    return 'Brute Force (T1110)'
    
    
def artifacts():
    try:
        return stats.collect(['source_security_id','error_message','destination_account_name','destination_account_domain','source_account_name','source_account_domain','event_id'])
    except Exception as e:
        raise e
        

def entity(event):
    return {'derived': False,
            'value': event.get('source_account_name'),
            'type': 'accountname'}