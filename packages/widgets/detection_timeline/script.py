# this to return default widget config
import time
import datetime


def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "properties": {"type": "bubble","layout": "conciselayout","onclick":"filter_apply"},
        "dimension": {"x": 4, "y": 0, "width": 8, "height": 2} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select * from fn_get_top_detection_counts",
        "parameters": {},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None

# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort():
    return {
"sortcol":"hour",
"sortorder":"asc"
}

# this to return return formated results to render a widget
def render(results):
    if not results or len(results) == 0:
        raise Exception("no results found")
    
    data = []
    for entry in results:
        entry_details = {
            'x': int(time.mktime(datetime.datetime.strptime(entry['hour'], '%Y-%m-%dT%H:%M:%S').timetuple()) * 1000),
            'y': entry['detectionname'],
            'z': entry['count'],
            'details': entry,  # Include modified entry in 'details'
            'detection': entry['detectionname']
        }
        data.append(entry_details)
    
    return {"results": data}