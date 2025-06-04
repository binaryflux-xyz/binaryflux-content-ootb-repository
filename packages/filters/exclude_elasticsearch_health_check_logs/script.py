def condition(event):
    message = event.get("event_message")
    process_name=event.get("process_name")
  
    if "http://localhost:9200/_cluster/health/" not in message and process_name!="AccessControlFilter" and process_name!="SchedulerService" :
        return True
    else:
        return False



