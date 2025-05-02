 #this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "pie","layout": "conciselayout"},
        "dimension": {"x": 8, "y": 4, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select event_outcome ,count(*) as actioncount from aggregation_table where event_outcome is not null and type = :type group by event_outcome",
        "parameters": {"type":"top_action_name"},
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
        "sortcol":"actioncount",
        "sortorder":"DESC"
    }

# this to return return formated results to render a widget
def render(data):
    transformed_data = []

    for item in data:
        transformed_data.append({
            "name": item["event_outcome"],
            "y": item["actioncount"]
        })
    
    return {"result":transformed_data}