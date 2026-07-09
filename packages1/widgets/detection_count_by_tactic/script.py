# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "pie","layout":"conciselayout","onclick":"filter_apply"},
        "dimension": {"x":4,"y":2,"width": 4, "height": 2}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select detectiontactic ,count(*) as tacticcount from entityscoring group by detectiontactic",
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
        "sortcol":"tacticcount",
        "sortorder":"DESC"
    }

# this to return return formated results to render a widget
def render(data):
    transformed_data = []

    for item in data:
        transformed_data.append({
            "name": item["detectiontactic"],
            "y": item["tacticcount"]
        })
    
    return {"result":transformed_data}