import time
import re
from collections import defaultdict

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "singlecolumn","onclick":"filter_apply"},
      # "filters":['secmark/default/widgetfilters/windows_host_filter/'],
        "dimension": {"x":0,"y":0,"width": 9, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select max(timestamp) as last_activity_time, count(*) as total_events, host from aggregation_table  where host is not null and type = :type group by host',
        'parameters': {"type":"tenant_health_monitor_breakdown"}
    }



def filters(filter):
    filterqueries = []
    parameters = {}
    if filter:
        if filter.get("host"):
            filterqueries.append("Hostname in (:host)")
            parameters["host"] = filter.get("host")
    return {"filterqueries": filterqueries, "parameters": parameters}



# this to return free text search query and its parameters
def search(freetext):
    return None


# this to return sort query
def sort():
    return None

def render(data):
    counter = 0
    categories = []
    series = []

    for item in data:
        if counter < 10:  # Change this number to set your limit
            categories.append(item["host"])
            series.append(item["total_events"])
            counter += 1
    
    return {"series": series, "categories": categories}