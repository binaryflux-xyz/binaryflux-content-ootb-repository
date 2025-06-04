import json
from datetime import datetime
import time
import re


def criteria(metainfo):
    return metainfo['provider'] == 'Microsoft' and metainfo['group'] == 'SQL Server' \
        and metainfo['type'] == 'Audit'


# Function to parse event time to timestamp
def timestamp(event):
    datestring = event["event_time"].replace("T", " ")
    dt = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S.%f")
    epoch_time = time.mktime(dt.timetuple()) + dt.microsecond / 1e6
    return int(epoch_time * 1000)


# Convert the event data to a combined dictionary
def message(event):
    if 'statement' in event and event['statement']:
        return event['statement']
    elif 'Message' in event and event['Message']:
        return event['Message']
    return None

# Build normalized dictionary for easier access and processing
def dictionary(event):
    event_dict = {}

    if "class_type" in event and event["class_type"]:
        event_dict["event_category"] = event["class_type"]

    if "application_name" in event and event["application_name"]:
        event_dict["application"] = event["application_name"]

    if "action_id" in event and event["action_id"]:
        event_dict["action_id"] = event["action_id"]

    if "action_name" in event and event["action_name"]:
        event_dict["action_name"] = event["action_name"]

    if "client_ip" in event and event["client_ip"]:
        event_dict["ip_address"] = event["client_ip"]

    if "database_principal_name" in event and event["database_principal_name"]:
        event_dict["database_principal_name"] = event["database_principal_name"]

    if "schema_name" in event and event["schema_name"]:
        event_dict["schema_name"] = event["schema_name"]

    if "affected_rows" in event and event["affected_rows"] is not None:
        event_dict["affected_rows"] = event["affected_rows"]

    if "server_instance_name" in event and event["server_instance_name"]:
        event_dict["server_instance_name"] = event["server_instance_name"]

    if "succeeded" in event:
        event_dict["action_status"] = event["succeeded"]

    if "target_server_principal_name" in event and event["target_server_principal_name"]:
        event_dict["target_server_principal_name"] = event["target_server_principal_name"]

    if "object_id" in event and event["object_id"] is not None:
        event_dict["object_id"] = event["object_id"]

    if "data_sensitivity_information" in event and event["data_sensitivity_information"]:
        event_dict["sensitive_information"] = event["data_sensitivity_information"]

    if "target_database_principal_name" in event and event["target_database_principal_name"]:
        event_dict["target_database_principal_name"] = event["target_database_principal_name"]

    if "user_defined_information" in event and event["user_defined_information"]:
        event_dict["user_defined_information"] = event["user_defined_information"]

    if "session_server_principal_name" in event and event["session_server_principal_name"]:
        event_dict["server_initiated_user_name"] = event["session_server_principal_name"]

    if "statement" in event and event["statement"]:
        cleaned_statement = re.sub(r'\s+', ' ', event["statement"]).strip()
        event_dict["statement"] = cleaned_statement

    if "database_name" in event and event["database_name"]:
        event_dict["database_name"] = event["database_name"]

    if "is_local_secondary_replica" in event:
        event_dict["is_local_secondary_replica"] = event["is_local_secondary_replica"]

    if "file_name" in event and event["file_name"]:
        event_dict["file_name"] = event["file_name"]

    if "server_principal_name" in event and event["server_principal_name"]:
        event_dict["server_principal_name"] = event["server_principal_name"]

    if "additional_information" in event and event["additional_information"]:
        event_dict["additional_information"] = event["additional_information"]

    if "object_name" in event and event["object_name"]:
        event_dict["event_type"] = event["object_name"]

    return event_dict