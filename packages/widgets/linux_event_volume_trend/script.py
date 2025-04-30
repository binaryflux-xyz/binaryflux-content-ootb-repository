from datetime import datetime, timedelta
from collections import OrderedDict
import time

# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "column","onclick":"not_open_offcanvaspanel"},
        "dimension": {"x": 0, "y": 0, "width": 9, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():

    query = """
        SELECT 
            (timestamp//3600000*3600000) AS event_time,
            COUNT(*) AS event_count
        FROM aggregation_table
        WHERE type = :type
        GROUP BY event_time
        ORDER BY event_time DESC
        LIMIT 48;
    """
    return {
        "query": query,
        "parameters": {"type":"host_health_status_linux_kaspersky"},
    }
# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    filterqueries = []
    parameters = {}
    if filter:
        if filter.get("host"):
            filterqueries.append("source_hostname in (:host)")
            parameters["host"] = filter.get("host")
    return {"filterqueries": filterqueries, "parameters": parameters}

# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort():
    return None


# this to return return formated results to render a widget

# this to return return formated results to render a widget
def render(results):
    
    trend_map = create_hour_map(parameters.get("endtime"))
    # print(trend_map)
    for result in results:
        trend_map[result['event_time']] = result['event_count']
    
    trend_map = OrderedDict(sorted(trend_map.items()))
    
    distinct_xaxis_array = [toHour(key) for key in trend_map.keys()]
    
    series = [{"data": trend_map.values(), "name": "events"}]

    return {"result":{"categories":distinct_xaxis_array,"series":series}}
  
def toHour(epoch) :
    try :
      dt = datetime.fromtimestamp(epoch/1000)
      return dt.strftime('%d %H')
    except Exception as e:
        return epoch
      
def create_hour_map(endlong) :
    trend_map = OrderedDict()
    epochmap = {}
    try:
        formatter = "%d %H"    

        end_time = datetime.fromtimestamp(endlong / 1000).replace(minute=0, second=0, microsecond=0)
        
        # Generate the last 48 hourly timestamps from end_date
        temp_time = end_time - timedelta(hours=47)  # Go back 47 hours to include end_date itself
        
        while temp_time <= end_time:
            epoch = int(time.mktime(temp_time.timetuple())*1000)
            trend_map[epoch] = 0
            temp_time += timedelta(hours=1)
            
    except Exception as e:
        print(str(e))
    
    return trend_map

  