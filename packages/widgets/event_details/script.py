# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "fatalwidget","layout": "conciselayout"},
        "dimension": {"x": 4, "y": 7, "width": 8, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT event_description AS eventdescription, kaspersky_event_category AS category,kaspersky_event_entity as entity,  kaspersky_event_action as action, count(*) AS count FROM aggregation_table WHERE event_description IS NOT NULL AND kaspersky_event_category IS NOT NULL AND kaspersky_event_entity IS NOT NULL AND kaspersky_event_action IS NOT NULL AND type = :type GROUP BY event_description, kaspersky_event_category, kaspersky_event_entity,kaspersky_event_action",
        "parameters": {"type":"top_event_details"},
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
        "sortcol":"count",
        "sortorder":"desc"    
    }


# this to return return formated results to render a widget
def render(results):
    if len(results) > 10:
        results = results[:10]  # Limit to the first five records        

    columnList=['eventdescription', 'category', 'entity','action','count'];
    
    return {"result": results,"columns":columnList}