import re

def transform(event):
    
    sentbytes = (
        int(event.get("network_bytes_out"))
        if event.get("network_bytes_out") is not None
        else 0
    )
    receivedbytes = (
        int(event.get("network_bytes_in"))
        if event.get("network_bytes_in") is not None
        else 0
    )

    bytesTransferred = sentbytes + receivedbytes
    event['network_bytes_transferred'] = bytesTransferred

    app = event.get('url') if event.get('url') is not None else \
            event.get('source_hostname') if event.get('source_hostname') is not None else None
    
    if app is not None :
        event['applicationname'] = app
    return event