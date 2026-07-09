import time
from datetime import datetime


# this to return True/False based on which this message will qualify to be used for datamodel
def criteria(metainfo):
    return metainfo['provider'] == 'mssql' and metainfo['group'] == 'audit' \
        and metainfo['type'] == 'database'


def timestamp(data):
    date_str=data['date']
    time_str=data['time']
    datetime_str = date_str + ' ' + time_str
    dt = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')
    timestamp_seconds = time.mktime(dt.timetuple())
    return int(timestamp_seconds * 1000)


def message(event):
    event_message = event.get("event")
    return event_message


# Dictonary
def dictionary(event):
    
    return {
        "source_ip": event.get("ip"),
        "user_name": event.get("user"),
        "process_command_line": event.get("event")
    }