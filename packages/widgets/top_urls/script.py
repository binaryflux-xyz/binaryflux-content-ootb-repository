# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "treemap","layout": "conciselayout"},
        "dimension": {"x": 4, "y": 4, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select url as name,count(*) as value from aggregation_table  where url is not null and type = :type group by url",
        "parameters": {"type":"top_events_data"},
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
        "sortcol":"value",
        "sortorder":"desc"    
    }

def render(result):
    if not result or len(result) == 0:
        raise Exception("no results found")
        
    return {"result": result, "type":"top_events_data"}
