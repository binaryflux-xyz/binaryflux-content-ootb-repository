# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "bar","layout": "conciselayout"},
        "dimension": {"x": 0, "y": 4, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT source_device_id AS device, count(*) AS total FROM aggregation_table WHERE source_device_id IS NOT NULL AND type = :type GROUP BY source_device_id",
        "parameters": {"type":"top_device_name"},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None

# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort():
    return{
        "sortcol":"total",
        "sortorder":"desc"    
    }

# this to return return formated results to render a widget
def render(result):
    data = []
    categories = []
    counter=0

    for item in result:
        if(counter<10):
            categories.append(item["device"])
            data.append(item["total"])
            counter=counter+1
        
    return {"series":[{'data':data}], 'categories': categories}