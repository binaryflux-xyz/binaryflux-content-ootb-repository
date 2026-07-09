import time
from datetime import datetime


# this to return True/False based on which this message will qualify to be used for datamodel
def criteria(metainfo):
    return metainfo['provider'] == 'microsoft' and metainfo['group'] == 'syslog' \
        and metainfo['type'] == 'audit'

def timestamp(event):
    datestring = event["EventTime"]
    dt = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")  # Parse the string to datetime
    epoch_time = time.mktime(dt.timetuple())  # Convert to seconds since epoch
    milliseconds = int(epoch_time * 1000)  # Convert to milliseconds
    return milliseconds


# this to return user readable text as message extracted from event
def message(event):
    return event.get('Message')    # return event_message


# Dictonary
def dictionary(event):
    event_dict={"event_id": event.get("EventID"),
    "event_category":event.get("Category"),
	"event_type": event.get("EventType"),
	"host": event.get("Hostname"),
	"source_account_name": event.get("SubjectUserName"),
	"source_account_domain": event.get("SubjectDomainName"),
	"source_security_id": event.get("SubjectUserSid"),
	"source_logon_id": event.get("SubjectLogonId"),
	"source_ip": event.get("IpAddress"),
	"source_port": event.get("IpPort"),
	"source_workstation":event.get("SourceName"),
	"source_modulename": event.get("SourceModuleName"),
	"source_moduletype": event.get("SourceModuleType"),
	
    
	# Destination information
	"destination_account_name": event.get("TargetUserName") ,
	"destination_account_domain": event.get("TargetDomainName") ,
	"destination_security_id": event.get("TargetUserSid"),
	"destination_logon_id": event.get("TargetLogonId"),

	# Process information
	"process_id": event.get("ProcessID"),
	"process_name": event.get("ProcessName"),

	"event_level": event.get("SeverityValue"),
	"event_severity": event.get("Severity"),


	# logoninformation
	"logon_type": event.get("LogonType") ,
	"logon_processname":event.get("LogonProcessName"),

}
    if "PrivilegeList" in event:
        event_dict["privileges"] = event.get("PrivilegeList")

    return event_dict