import time
import datetime


# this to return True/False based on which this message will qualify to be used for datamodel
def criteria(metainfo):
    return metainfo['provider'] == 'microsoft' and metainfo['group'] == 'security' \
        and metainfo['type'] == 'system'

def timestamp(event):
    header = event.get("header")
    if header is None:
        print("Header is None")
        return None

    date = header.get('date')
    if date is None:
        print("Date is None")
        return None

    current_year = str(datetime.datetime.now().year)
    datestring = date + ' ' + header.get('time') + ' ' + current_year

    element = datetime.datetime.strptime(datestring, "%b %d %H:%M:%S %Y")
    timestamp = time.mktime(element.timetuple()) * 1000
    return int(timestamp)


# this to return user readable text as message extracted from event
def message(event):
    return event.get('header').get('description')
    # return event_message


# Dictonary
def dictionary(event):
    creatorsubject = event.get("creatorsubject", {})
    subject = event.get("subject", {})
    newlogon = event.get("newlogon", {})
    networkinformation = event.get("networkinformation", {})
    filterinformation = event.get("filterinformation", {})
    process = event.get("process", {})
    processinformation = event.get("processinformation", {})
    service = event.get("service", {})
    shareinformation = event.get("shareinformation", {})
    logoninformation = event.get("logoninformation", {})
    targetsubject = event.get("targetsubject", {})
    accountwhosecredentialswereused = event.get(
        "accountwhosecredentialswereused", {})
    accountforwhichlogonfailed = event.get("accountforwhichlogonfailed", {})
    targetserver = event.get("targetserver", {})
    failure_reason = event.get("failureinformation", {})
    directoryservice = event.get("directoryservice", {})
    serviceinformation = event.get("serviceinformation", {})
    changedattributes = event.get("changedattributes", {})
    attributes = event.get("attributes", {})
    directory_object = event.get("object", {})
    operation = event.get("operation", {})
    newaccount = event.get("newaccount", {})
    ruleinformation = event.get("ruleinformation", {})
    rule=event.get("rule", {})
    errorinformation = event.get("errorinformation", {})
    additionalinformation = event.get("additionalinformation", {})
    values=additionalinformation.get("values",[])
    accountinformation=event.get("accountinformation", {})
    accessrequestinfromation = event.get("accessrequestinfromation", {})
    applicationinformation=event.get("applicationinformation", {})
    requestedoperation=event.get("requestedoperation", {})

    # Source information
    return modify({
        "rule_id":ruleinformation.get("id") or rule.get("id"),
        "rule_name":ruleinformation.get("name") or rule.get("name"),
        "host": event.get("header").get("host"),
        "error_message": failure_reason.get("failure_reason") or errorinformation.get("reason") or event.get("reasonforrejection"),
        "event_id": event.get("header").get("event_id"),
        "event_type": event.get("header").get("event_type"),
        "source_account_name": newlogon.get("account_name") or creatorsubject.get("account_name") or subject.get("account_name") or accountinformation.get("account_name"),
        "source_account_domain": newlogon.get("account_domain") or creatorsubject.get("account_domain") or subject.get("account_domain")  or accountinformation.get("account_domain"),
        "source_security_id": newlogon.get("security_id") or creatorsubject.get("security_id") or subject.get("security_id"),
        "source_logon_id": newlogon.get("logon_id") or creatorsubject.get("logon_id") or subject.get("logon_id") or event.get("logonaccount"),
        "source_logon_guid": newlogon.get("logon_guid") or subject.get("logon_guid"),
        "source_ip": networkinformation.get("source_network_address") or networkinformation.get("source_address"),
        "source_port": networkinformation.get("source_port"),
        "user_account_control": changedattributes.get("user_account_control") or attributes.get("user_account_control"),
        "ldap_display_name": attributes.get("ldap_display_name"),
        "operation_type": operation.get("type"),
        "source_workstation":event.get("sourceworkstation"),
        "applicationname": applicationinformation.get("applicationname"),

        # Destination information
        "destination_account_name": targetsubject.get("account_name") or accountwhosecredentialswereused.get("account_name") or accountforwhichlogonfailed.get("account_name") or newaccount.get("account_name"),
        "destination_account_domain": targetsubject.get("account_domain") or accountwhosecredentialswereused.get("account_domain") or accountforwhichlogonfailed.get("account_domain") or newaccount.get("account_domain"),
        "destination_security_id": targetsubject.get("security_id") or accountforwhichlogonfailed.get("security_id") or newaccount.get("security_id"),
        "destination_logon_id": targetsubject.get("logon_id") or accountwhosecredentialswereused.get("logon_id"),
        "destination_logon_guid": targetsubject.get("logon_guid") or accountwhosecredentialswereused.get("logon_guid"),
        "destination_server_name": targetserver.get("target_server_name"),
        "destination_ip": networkinformation.get("destination_address") or networkinformation.get("client_address"),
        "destination_port": networkinformation.get("destination_port") or networkinformation.get("client_port"),
        "network_protocol": networkinformation.get("protocol"),

        # Process information
        "process_command_line": event.get("processcommandline"),
        "process_id": process.get("process_id") or processinformation.get("new_process_id") or processinformation.get("process_id") or processinformation.get("caller_process_id"),
        "process_name": process.get("process_name") or processinformation.get("new_process_name") or processinformation.get("process_name") or processinformation.get("caller_process_name"),
        "creator_process_id": processinformation.get("creator_process_id"),
        "creator_process_name": processinformation.get("creator_process_name"),

        # Server information
        "server": service.get("server") or  directory_object.get("object_server"),
        "service_address": networkinformation.get("network_address") or networkinformation.get("source_network_address"),
        "service_port": networkinformation.get("port"),
        "server_workstation": networkinformation.get("workstation_name"),
        "process_io_type": networkinformation.get("object_type"),
        "service_name": directoryservice.get("name") or serviceinformation.get("service_name") or directory_object.get("object_name"),
        "service_type": directoryservice.get("type") or serviceinformation.get("service_type") or directory_object.get("object_type"),

        # Object Information
        "object_dn": directory_object.get("dn"),
        "object_guid": directory_object.get("guid"),
        "object_class": directory_object.get("class"),

        # share inofrmation
        "io_type_name": shareinformation.get("share_name"),
        "io_type_path": shareinformation.get("share_path"),
        "io_type_relative_destination_path": shareinformation.get("relation_destination_path"),

        # logoninformation
        "logon_type": logoninformation.get("logon_type") or event.get("logontype"),
        "layer_name":filterinformation.get("layer_name"),
        "descriptions": values[0] if values else None,
        "access":accessrequestinfromation.get("accesses") or requestedoperation.get("privileges"),

    })


def remove_quotes(input_string):
    if not input_string or len(input_string) < 2:
        return input_string  # Return as is if empty or too short to have surrounding quotes

    # Check for both single and double quotes
    if (input_string.startswith(("'", '"')) and input_string.endswith(("'", '"')) and input_string[0] == input_string[-1]):  
        return input_string[1:-1]
    
    return input_string 

def modify(input):
    for key,value in input.items():
        if isinstance(value, str):
            input[key] = remove_quotes(value)
    return input
