# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "area","layout": "conciselayout","onclick":"filter_not_apply"},
        "dimension": {"x": 8, "y": 4, "width": 4, "height": 2} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT * FROM fn_getstreamincidentcounts",
        "parameters": {'n' : 0},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None

# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort():
    return None

# this to return return formated results to render a widget
def render(result):
    data = []
    categories = []
    counter=0

    for item in result:
        if(counter<10):
            categories.append(item["stream_name"])
            data.append(item["incidents_count"])
            counter=counter+1
        
    return {"series":[{'data':data,'name':''}], 'categories': categories}