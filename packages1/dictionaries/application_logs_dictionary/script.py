import re
import time
import datetime

def parse_and_print_log_json(data):
    log_line = data.get("logEvent").get("message")

    pattern_text = r'''
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})\s+
    (?P<level>[A-Z]+)\s+
    \[(?P<thread>[^\]]+)\]\s+
    (?P<component>[^:]+):\s+
    (?P<message>.+?)(?=\n\t|$)
    '''

    pattern = re.compile(pattern_text, re.VERBOSE | re.DOTALL)
    match = pattern.search(log_line)

    if match:
        return match.groupdict()
    else:
        return None


def criteria(metainfo):
    return metainfo['provider'] == 'AWS' and \
           metainfo['group'] == 'S3' and \
           metainfo['type'] == 'File Access' and \
           metainfo['name'] == 'Application Logs'


def timestamp(data):
    event = parse_and_print_log_json(data)
    ts = event.get("timestamp")
    dt = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S,%f')
    epoch_seconds = time.mktime(dt.timetuple())
    millis = int(epoch_seconds * 1000 + dt.microsecond / 1000.0)
    return millis
  


def message(data):
    event = parse_and_print_log_json(data)
    if event:
        return event.get("message")
    else:
        return None



def dictionary(rawdata):
    event=parse_and_print_log_json(rawdata)
    return  {
    "event_severity":event.get("level"),
    "process_thread_name":event.get("thread"),
    "process_name": event.get("component"),
    "event_message": event.get("message"),
        
    }