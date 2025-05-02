# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "eventtype_stats","layout": "conciselayout"},
        "dimension": {"x": 0, "y": 0, "width": 12, "height": 1} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select event_description as description ,count(*) as total from aggregation_table where event_description is not null and type = :type group by event_description",
        "parameters": {"type":"eventstat_data"},
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
def render(results):
    return {"result":results}