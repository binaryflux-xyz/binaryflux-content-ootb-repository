import time
import datetime

def criteria(metainfo):
    return metainfo['provider'] == 'AWS' and metainfo['group'] == 'S3' \
        and metainfo['type'] == 'File Access' and  metainfo['name'] == 'Virtual Private Cloud'


def parse_vpc_flow_log(data):
    log_message=data.get("logEvent").get("message")
    
    fields = log_message.strip().split()
    
    return fields


def timestamp(data):
    event = parse_vpc_flow_log(data)
    
    epoch_time = event[10]
    return int(epoch_time) * 1000  # Convert to milliseconds
  


def message(event):
    return "message"


def dictionary(rawdata):
    event=parse_vpc_flow_log(rawdata)
    try:
        bytes_transferred = float(event[9]) if event[9] != '-' else 0.0
    except (ValueError, TypeError):
        bytes_transferred = 0.0

    return {
    "account_id":event[1],
    "interface_id":event[2],
    "source_ip": event[3],
    "destination_ip": event[4],
    "source_port": event[5],
    "destination_port": event[6],
	"total_packets_exchanged":event[8],
	"total_bytes_transferred":bytes_transferred,
	"event_action": event[12],
	"event_status":event[13],
	"details": {
            'protocol_num': event[7]
        },
        
    }