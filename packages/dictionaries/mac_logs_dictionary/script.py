import time
from datetime import datetime

# This function determines if the log qualifies for data processing.
def criteria(metainfo):
    return metainfo.get('provider') == 'apple' and metainfo.get('group') == 'syslog' \
        and metainfo.get('type') == 'audit'

def timestamp(event):
    datestring = event["message"]["timestamp"]  # Extract timestamp
    # Remove the timezone part (last 5 characters) and just parse the datetime
    dt_str = datestring[:-5]  # Remove the timezone part (e.g., +0000)

    # Parse the datetime without the timezone
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")

    # Convert to seconds since epoch
    epoch_time = time.mktime(dt.timetuple()) + dt.microsecond / 1e6  # Use timetuple and add microseconds
    milliseconds = int(epoch_time * 1000)  # Convert to milliseconds

    return milliseconds

# Extracts user-readable message from event
def message(event):
    return "mac logs" # Extract the event message

# Dictionary function for structured event data
def dictionary(event):
    event_dict = {
        "event_type": event["message"].get("eventType"), 
        "event_category": event["message"].get("category"),
        "host": event.get("host"),
        "format_string": event["message"].get("formatString"),
        "subsystem": event["message"].get("subsystem"),
        "event_Message":event["message"].get("eventMessage"),
        "source_image_uuid": event["message"].get("senderImageUUID"),
        "source_image_path": event["message"].get("senderImagePath"),
        "process_id": event["message"].get("processID"),
        "process_image_uuid": event["message"].get("processImageUUID"),
        "process_image_path": event["message"].get("processImagePath"),
        "thread_id": event["message"].get("threadID"),
        "trace_id": event["message"].get("traceID"),
        "activity_id": event["message"].get("activityIdentifier"),
    }

    return event_dict
