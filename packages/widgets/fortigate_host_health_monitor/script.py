import time
# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": True,
        "datepicker": True,
        "properties": {"type": "table","onclick":"filterapply"},
        "dimension": {"x":0,"y":0,"width": 4, "height": 8}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select max(timestamp) as last_activity_time , count(*) as total_events, source_device_name as host from aggregation_table  where source_device_name is not null and type = :type group by source_device_name',
        'parameters': {"type":"host_health_status_fortigate"}
    }



# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    searchquery = ' "source_device_name" ilike :source_device_name '
    return {
        'searchquery': searchquery,
        'parameters': {'source_device_name': '%' + freetext + '%'},
    }


# this to return sort query
def sort():
    return{
        "sortcol":"last_activity_time",
        "sortorder":"desc"    
    }


def render(results):

    if not results or len(results) == 0:
        raise Exception("no results found")
    
    for result in results:
        result['LastSeen'] = getTimePhrase(result['last_activity_time'])

    rows = []
    columns = ['host' , 'LastSeen', 'total_events']

    return  {"result":{"columns": columns, "rows": results},"column":"host","label":"Server","uniquekey":['host'],"columnmap":["host"]}

def getTimePhrase(activitytime):
    
    timediff = round(time.time()*1000) - activitytime

    if timediff < 60000:  # Less than 60 sec
        return "{} sec ago".format(int(timediff / 1000))
    elif timediff < 3600000:  # Less than 60 min
        return "{} min ago".format(int(timediff / 60000))
    elif timediff < 86400000:  # Less than 24 hrs
        return "{} hrs ago".format(int(timediff / 3600000))
    else:
        return "{} days ago".format(int(timediff / 86400000))