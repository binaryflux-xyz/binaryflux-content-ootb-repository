import time
import datetime

# this to return True/False based on which this message will qualify to be used for datamodel
def criteria(metainfo):
    return metainfo['provider'] == 'kaspersky' and metainfo['group'] == 'firewall' \
        and metainfo['type'] == 'network'


# this to return time of event 

def timestamp(event):
    #2024-12-10T04:40:30.000Z
    datestring = event['iso_timestamp']
    element = datetime.datetime.strptime(datestring,"%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp = time.mktime(element.timetuple())
    return int(timestamp)
    


def message(event):
    if not event:
        return "Event data is missing."
    else:
        event = {key: value for key, value in event.items() if value is not None}

    # Extract relevant details from the event dictionary
    application = event.get("application", "Unknown Application")
    event_type = event.get("event_type", "Unknown Event Type")
    event_description = event.get("event_description", "No Description Available")
    user = event.get("user", "Unknown User")
    url = event.get("url", "No URL Provided")
    result = event.get("result", "No Result Provided")
    rule = event.get("rule", "No Rule Information")
    content_category = event.get("content_category", "No Category")
    source = event.get("content_category_source", "Unknown Source")
    ip = event.get("hip", "No IP Address")
    host = event.get("hdn", "Unknown Host")
    process_id = event.get("process_id", "Unknown Process ID")
    exe_name = event.get("exe_name", "Unknown Executable")
    app_path = event.get("app_path", "Unknown Application Path")

    # Construct the message
    result_message = (
        "An event was detected by the " + application + " application on host '" + host + "' with IP address " + ip + ". "
        "The event, categorized as '" + event_description + "', occurred when the user '" + user + "' attempted to access "
        "the URL '" + url + "'. This action was blocked as per the applied rule '" + rule + "', which enforces restrictions "
        "on content categorized as '" + content_category + "', based on data provided by the " + source + " source. "
        "The specific event type, '" + event_type + "', indicates that this action violated security policies or standards "
        "established for web communications. The executable involved in this operation was '" + exe_name + "', located at '" + app_path + "', "
        "and the process ID associated with this request was " + process_id + ". The block action ensures compliance with security protocols "
        "to prevent unauthorized or risky web communications. This incident highlights the effectiveness of active web controls and rule enforcement."
    )

    return result_message


# this to return attribute map to be indexed for this event
def dictionary(event):
    return {
        # Policy information
        "log_syslog_priority":event.get("priority"),
        "log_syslog_hostip": event.get("hip"),
        "host_name": event.get("hostname"),
        "threat_enrichments_indicator_name": event.get("hdn"),
        "log_syslog_version":event.get("log_version"),
        "log_syslog_appname": event.get("app_name"),
        "log_syslog_app": event.get("application"),
        # "application": event.get("application"),
        "event_type": event.get("event_type"),
        "event_description": event.get("etdn"),
        "log_syslog_apppath":event.get("app_path"),
        "log_syslog_procid": event.get("process_id"),
        "user_name": event.get("user"),
        "event_outcome": event.get("result"),
        "url":event.get("url"),
        "rule_name": event.get("rule"),
        "category_name": event.get("content_category"),
        "category_source": event.get("category_source"),
        "event_action": event.get("tdn"),
        "group_name": event.get("gn"),
        "event_address": event.get("address_mask"),      
        "source_device_name":event.get("device_category"),
        "source_device_id": event.get("device_id"),
        "source_device_type":event.get("device_type_bus_type"),
      
        
    
        # Additional details
        "details": {
            #  p1 of event for kaspersky
             "kaspersky_event_category": event.get("p1"), 
              #  p2 of event for kaspersky
             "kaspersky_event_entity": event.get("p2"), 
              #  p3 of event for kaspersky
             "kaspersky_event_action": event.get("p3"), 
             "execute_file":event.get("exe_name"),
             "version_code":event.get("version_code"),
             "device_vid_pid":event.get("device_vid_pid")
        },
    }