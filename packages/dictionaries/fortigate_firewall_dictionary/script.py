import time
from datetime import datetime

# this to return True/False based on which this message will qualify to be used for datamodel
def criteria(metainfo):
    return metainfo['provider'] == 'fortigate' and metainfo['group'] == 'firewall' \
        and metainfo['type'] == 'network'


# this to return time of event 
def timestamp(event):
    """
    Convert event time to milliseconds since the Unix epoch.

    Args:
        event (dict): Dictionary containing the event information, including the event time.

    Returns:
        int: Milliseconds since the Unix epoch representing the event time.
    """
    datestring = event.get("eventtime")
    
    if datestring is None:
        # Handle the case where eventtime is not provided or is None
        return None  # Or raise an error, depending on your requirements

    if len(datestring) > 13:
        # If the date string length is greater than 13, it's likely in nanoseconds.
        element = int(event.get("eventtime")) / 1e9
        # Convert nanoseconds to seconds and create a datetime object.
        dt_object = datetime.utcfromtimestamp(element)
        # dt_object = datetime.datetime.fromtimestamp(element, tz=timezone.utc)
        # Convert datetime object to a timestamp string with milliseconds.

        dt_string = str(dt_object)
        new_dt = dt_string[:19]
        timestamp = datetime.strptime(new_dt, "%Y-%m-%d %H:%M:%S")
        # Convert the timestamp string to milliseconds since the Unix epoch and return.
        return (
            int(time.mktime(timestamp.timetuple()) + timestamp.microsecond / 1e6) * 1000
        )

    elif len(datestring) <= 10:
        # If the date string length is 10 or less, it's likely in seconds.
        element = int(event.get("eventtime"))
        # Create a datetime object from the timestamp in seconds.
        dt_object = datetime.utcfromtimestamp(element)
        # dt_object = datetime.datetime.fromtimestamp(element, tz=timezone.utc)
        # Convert datetime object to a timestamp string.
        dt_string = str(dt_object)
        new_dt = dt_string[:19]
        timestamp = datetime.strptime(new_dt, "%Y-%m-%d %H:%M:%S")
        # Convert the timestamp string to milliseconds since the Unix epoch and return.
        return (
            int(time.mktime(timestamp.timetuple()) + timestamp.microsecond / 1e6) * 1000
        )

    else:
        # If the date string length doesn't match any known formats, return the original value.
        return int(event.get("eventtime"))
    

def message(event):
    """
    Generate a message based on the event information.
    
    Args:
        event (dict): Dictionary containing the event information, including message ("msg"), type ("type"), and subtype ("subtype").
        
    Returns:
        str: Generated message.
    """
    # Retrieve the message from the event dictionary, or construct a default message if it's None.
    event_message = event.get("msg")
    
    if event_message:
        if isinstance(event_message, dict):
            alert_id = event_message.get("virusid")
            if alert_id:
                resultmessage = "Alert #" + alert_id + ": '" + event_message.get("virus") + "' has been identified. Type: " + event_message.get("dtype") + ". Score: " + str(event_message.get("crscore")) + ". Severity: " + event_message.get("crlevel") + "."
            else:
                resultmessage = event_message
        else:
            resultmessage = event_message
    else:
        resultmessage = "Message with type " + str(event.get("type")) + " and subtype " +  str(event.get("subtype"))
        
    return resultmessage

   


# this to return attribute map to be indexed for this event
def dictionary(event):
    """
    Convert event details into a dictionary format for easy access.
    
    Args:
        event (dict): Dictionary containing the event information.
        
    Returns:
        dict: Dictionary containing the event details organized by categories.
    """
    return modify({
        # Policy information
        "policy_name": event.get("policyname"),
        "policy_id": event.get("policyid"),
        "policy_type": event.get("policytype"),
        
        # Event details
        "log_id": event.get("logid"),
        "log_type": event.get("type"),
        "log_subtype": event.get("subtype"),
        
        # Alert information
        "alert_id": event.get("virusid"),
        "alert_name": event.get("virus"),
        "alert_type": event.get("dtype"),
        "alert_score": event.get("crscore"),
        "alert_severity": event.get("crlevel"),
       
        # Event details continued
        "event_id": event.get("eventid"),
        "event_type": event.get("eventtype"),
        "event_subtype": event.get("subtype"),
        "event_duration": event.get("duration"),
        "event_category_id": event.get("cat"),
        "event_category_desc": event.get("catdesc"),
        "event_level": event.get("level"),
        "event_severity": event.get("severity"),
        "event_outcome": event.get("categoryoutcome"),
        "event_sessionid": event.get("sessionid"),
        "event_action": event.get("action"),
        
        # Source information
        "source_port": event.get("srcport"),
        "source_ip": event.get("srcip"),
        "source_name": event.get("srcname"),
        "source_remote_ip": event.get("remip"),
        "source_remote_port": event.get("remport"),
        "source_hostname": event.get("hostname"),
        "source_mac_address": event.get("srcmac"),
        "source_country": event.get("srccountry"),
        "source_device_category": event.get("devcategory"),
        "source_device_name": event.get("devname"),
        "source_device_id": event.get("devid"),
        "source_device_type": event.get("devtype"),
        "source_device_interface": event.get("srcintf"),
        "source_server": event.get("srcserver"),
        "source_family": event.get("srcfamily"),
        
        # Destination information
        "destination_port": event.get("dstport"),
        "destination_ip": event.get("dstip"),
        "destination_device_interface": event.get("dstintf"),
        "destination_hostname": event.get("qname"),
        "destination_country": event.get("dstcountry"),
        "destination_device_type": event.get("dstdevtype"),
        "destination_server": event.get("dstserver"),
        "destination_family": event.get("dstfamily"),
        
        # User information
        "os_name": event.get("osname"),
        "user_name": event.get("user"),
        "user_group": event.get("group"),
        "user_role": event.get("profile"),
        "user_agent": event.get("agent"),
        
        # Network information
        "network_protocol": event.get("service"),
        "network_direction": event.get("dir") or event.get("direction"),
        "network_encryption": event.get("encryption"),
        "network_request_method": event.get("method"),
        "network_icmpid": event.get("icmpid"),
        "network_icmpid_code": event.get("icmpcode"),
        "network_cookies": event.get("cookies"),
        "network_bytes_in": event.get("rcvdbyte"),
        "network_bytes_out": event.get("sentbyte"),
        "network_packets_in": event.get("rcvdpkt"),
        "network_packets_out": event.get("sentpkt"),
        "network_status": event.get("status"),
        
        # File information
        "file_extension": event.get("filetype"),
        "file_name": event.get("filename"),
        "file_size": event.get("filesize"),
        
        # VoIP information
        "voip_phonenumber": event.get("phonenumber"),
        "voip_carrier": event.get("carrier"),
        "voip_plan": event.get("plan"),
        
        # Application information
        "application_risk": event.get("apprisk"),
        "application_category": event.get("appcat"),
        "applicationname": event.get("app"),
        "application_id": event.get("appid"),
        "application_control_profile": event.get("applist"),
        "source_hw_vendor":event.get("srchwvendor"),
        "source_hw_version":event.get("srchwversion"),
        "url":event.get("url"),
        
        # Additional details
        "details": {
            "vdname": event.get("vd"),
            "proto": event.get("proto"),
            "xauthuser": event.get("xauthuser"),
            "xauthgroup": event.get("xauthgroup"),
            "wanin": event.get("wanin"),
            "wanout": event.get("wanout"),
            "lanin": event.get("lanin"),
            "lanout": event.get("lanout"),
            "local": event.get("locip"),
            "locport": event.get("locport"),
            "vpn":event.get("vpn"),
            "vpntype":event.get("vpntype")
        },
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

