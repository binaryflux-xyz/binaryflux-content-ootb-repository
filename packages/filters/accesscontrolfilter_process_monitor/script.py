def condition(event):

    process_name=event.get("process_name")
    if process_name == "AccessControlFilter" and process_name!="SchedulerService" :
        return True
    else:
        return False


