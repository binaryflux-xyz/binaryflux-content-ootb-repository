# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "map"},
        "dimension": {"x": 0, "y": 26, "width": 8, "height": 5}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select * from fn_topqueues",
        "parameters": {}
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    
    return None

# this to return free text search query and its parameters
def search(freetext):
    
    return None

# this to return sort query
def sort(sorcol, sortorder):
    return None

# this to return return formated results to render a widget
def render(results):
    return  {"result":results} 