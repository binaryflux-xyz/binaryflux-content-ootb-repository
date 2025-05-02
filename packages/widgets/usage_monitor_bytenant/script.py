import time
import re
from collections import defaultdict
from datetime import datetime, timedelta


# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "bnfxserverdata","layout":"backgroundchanges"},
        "dimension": {"x":0,"y":1,"width": 12, "height": 10}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return [{
        'query': 'SELECT max(timestamp) as last_activity_time, tenant, COUNT(*) AS total_events, COUNT(DISTINCT host) AS distinct_hosts FROM aggregation_table WHERE tenant IS NOT NULL AND provider IS NOT NULL AND type = :type  AND  CAST(TO_TIMESTAMP(timestamp / 1000) AS DATE) = CURRENT_DATE    GROUP BY tenant;',
        'parameters': {"type":"tenant_health_monitor_breakdown"}
    },
  {
  "query": "SELECT CAST(DATE_TRUNC('hour', TO_TIMESTAMP(timestamp / 1000)) AS VARCHAR) AS hour, tenant, COUNT(*) AS total_events FROM aggregation_table WHERE tenant IS NOT NULL AND type = :type AND CAST(TO_TIMESTAMP(timestamp / 1000) AS DATE) = CURRENT_DATE GROUP BY tenant, hour ORDER BY tenant, hour;",
  "parameters": {
    "type": "tenant_health_monitor_breakdown"
  }
}]



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
    
    currTime = round(time.time()*1000)

    merged_data = defaultdict(lambda: {"last_activity_time": 0, "total_events": 0})

    for entry in results[0]:
        tenant = normalize_host(entry["tenant"])
        data = merged_data[tenant]  # Avoid multiple dictionary lookups

        data["total_events"] += entry.get('total_events',0)
        data["last_activity_time"] = max(data["last_activity_time"], entry.get('last_activity_time',0))
        data["distinct_hosts"] = entry['distinct_hosts']
    
    finalResult = map(lambda result: process_entry(result, currTime), merged_data.iteritems())  
  
    columns = ["datacenter", "lastEvent", "value", "serverstatus","devices","eph"]

  
    trendata=build_tenant_hourly_data(results[1])


    # return  {"series":list(finalResult),"columns":columns,"graphdata":trendata}
    return  {"series":list(finalResult),"columns":columns,"column":"tenant","label":"Device","uniquekey":['datacenter'],"columnmap":["tenant"],"graphdata":trendata}

def build_tenant_hourly_data(data):

    grouped = defaultdict(lambda: defaultdict(int))
    for entry in data:
        raw_hour = entry["hour"][:19]  # Slicing instead of splitting
        dt = datetime.strptime(raw_hour, "%Y-%m-%d %H:%M:%S")
        hour_key = dt.strftime("%m %H:00")
        grouped[entry["tenant"]][hour_key] = entry["total_events"]

    start = datetime(2025, 4, 9, 0)
    categories = [(start + timedelta(hours=i)).strftime("%m %H:00") for i in range(24)]

    result = {}
    for tenant in grouped:
        hourly_data = [grouped[tenant].get(hour, 0) for hour in categories]
        result[tenant] = {
            "categories": categories,
            "data": hourly_data
        }

    return result

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
        "devices": data["distinct_hosts"] ,
       "eph": format_number(data["total_events"] / 24)
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