import time
import datetime

# this to return True/False based on which this message will qualify to be used for datamodel
def criteria(metainfo):
    return metainfo['provider'] == 'linux' and metainfo['group'] == 'security' \
        and metainfo['type'] == 'system'


def timestamp(event):
    datestring = event['timestamp']
    
    try:
        # Try ISO 8601 format first (e.g., 2024-05-08T15:56:53.689231+05:30)
        datestring = datestring[:19]  # Truncate microseconds and timezone
        dt = datetime.datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S")
    
    except ValueError:
        # Fallback to log format (e.g., Apr  2 01:05:02)
        now = datetime.datetime.now()
        year = now.year
        full_time_str = ""+str(year)+" "+datestring
        dt = datetime.datetime.strptime(full_time_str, "%Y %b %d %H:%M:%S")
        
        # If parsed time is in the future, it probably belongs to the previous year
        if dt > now:
            year -= 1
            full_time_str = ""+str(year)+" "+datestring
            dt = datetime.datetime.strptime(full_time_str, "%Y %b %d %H:%M:%S")
    
    return int(time.mktime(dt.timetuple()) * 1000)


# this to return user readable text as message extracted from event
def message(event):
    return event.get('message').get('content') if event.get('message') else None
    # return event_message


# Dictonary
def dictionary(event):
    
    
    # Source information
    return {
        "event_severity": event.get("severity"),
        "source_hostname": event.get("hostname"),
        "process_id":event.get("procid"),
        "applicationname": event.get("appname"),
        "event_message": event.get("message").get("content"),
        "event_tag": event.get("message").get("tag"),
        "structured_data": event.get("structured_data"),
        "facility_name": event.get("facility"),
        
    }
