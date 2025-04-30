# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": True,
        "properties": {"type": "donut","layout": "conciselayout","onclick":"filter_apply"},
        "dimension": {"x": 4, "y": 4, "width": 4, "height": 2} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select detectioncriticality,count(*) as criticalitycount from entityscoring group by detectioncriticality",
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
        "sortcol":"criticalitycount",
        "sortorder":"DESC"
    }

# this to return return formated results to render a widget
def render(results):
    series = {item["detectioncriticality"]: item["criticalitycount"] for item in results if item["detectioncriticality"] != "NONE"}

    return {"result": series}