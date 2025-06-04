import json
from datetime import datetime
import time

def criteria(metainfo):
    return metainfo['provider'] == 'Omnifin' and metainfo['group'] == 'Application DB' \
        and metainfo['type'] == 'MYSQL'

# Function to parse event time to timestamp
def timestamp(event):
    datestring = event["event_time"]
    dt = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
    epoch_time = time.mktime(dt.timetuple())
    return int(epoch_time * 1000)


# Convert the event data to a combined dictionary
def message(event):
    if 'argument' in event and event['argument']:
        return event['argument']
    return None

def dictionary(event):
    event_dict = {}

    if "event_time" in event and event["event_time"]:
        event_dict["event_time"] = event["event_time"]

    if "argument" in event and event["argument"]:
        event_dict["event"] = event["argument"]

    if "command_type" in event and event["command_type"]:
        event_dict["action"] = event["command_type"]

    if "user_host" in event and event["user_host"]:
        event_dict["host_name"] = event["user_host"]
        
    if "thread_id" in event and event["thread_id"] is not None:
        event_dict["thread_id"] = event["thread_id"]
    
    if "server_id" in event and event["server_id"] is not None:
        event_dict["server_id"] = event["server_id"]

    return event_dict