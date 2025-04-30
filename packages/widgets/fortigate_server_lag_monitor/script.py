import time
import re
from collections import defaultdict

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "liveserverdata","filterid":"host",},
        "dimension": {"x":0,"y":3,"width": 12, "height": 6}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select max(timestamp) as last_activity_time, count(*) as total_events, source_device_name as host from aggregation_table  where source_device_name is not null and type = :type group by source_device_name',
        'parameters': {"type":"host_health_status_fortigate"}
    }



# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    return None


# this to return sort query
def sort():
    return None

def render(results):
    
    if not results or len(results) == 0:
        raise Exception("no results found")
    
    currTime = round(time.time()*1000)

    merged_data = defaultdict(lambda: {"last_activity_time": 0, "total_events": 0})

    for entry in results:
        host = normalize_host(entry["host"])
        data = merged_data[host]  # Avoid multiple dictionary lookups

        data["total_events"] += entry.get('total_events',0)
        data["last_activity_time"] = max(data["last_activity_time"], entry.get('last_activity_time',0))
    
    finalResult = map(lambda result: process_entry(result, currTime), merged_data.iteritems())  
  
    columns = ["datacenter", "lastEvent", "value", "source", "location","serverstatus","TotalEvents"]


    return  {"series":list(finalResult),"columns":columns,"column":"source_device_name","label":"City","uniquekey":['datacenter'],"columnmap":["source_device_name"]}

def normalize_host(host):
    """Remove surrounding quotes if present and ensure consistency."""
    return re.sub(r'^["\']|["\']$', '', host)

def process_entry(item, currTime):
    host, data = item
    timediff = currTime - data["last_activity_time"]

    return {
        "value": format_number(data["total_events"]),
        "lastEvent": getTimePhrase(timediff),
        "datacenter": host,
        "serverstatus": (
            "serverOnline" if timediff < 3600000 else 
            "serverUnstable" if timediff < 21600000 else 
            "serverOffline"
        ),
        "source": "fortigate"
    }

def getTimePhrase(timediff):
    seconds = int(timediff // 1000)
    minutes = int(seconds // 60)
    hours = int(minutes // 60)
    days = int(hours // 24)

    if minutes < 1:
        return "{} sec ago".format(seconds)
    elif hours < 1:
        return "{} min ago".format(minutes)
    elif days < 1:
        remaining_minutes = minutes % 60
        return "{} hr {} min ago".format(hours, remaining_minutes) if remaining_minutes else "{} hr ago".format(hours)
    else:
        remaining_hours = hours % 24
        return "{} days {} hr ago".format(days, remaining_hours) if remaining_hours else "{} days ago".format(days)


def format_number(num):
    if num >= 1000000000000:  # Trillions (T)
        return "%.2f T" % (num / 1000000000000.0)
    elif num >= 1000000000:  # Billions (B)
        return "%.2f B" % (num / 1000000000.0)
    elif num >= 1000000:  # Millions (M)
        return "%.2f M" % (num / 1000000.0)
    elif num >= 1000:  # Thousands (K)
        return "%.2f K" % (num / 1000.0)
    else:
        return str(num)  # No formatting for small numbers