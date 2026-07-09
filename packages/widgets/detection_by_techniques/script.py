# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "singlecolumn","layout":"conciselayout","onclick":"filter_apply"},
        "dimension": {"x":8,"y":2,"width": 4, "height": 2}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select detectiontechnique ,count(distinct detectionname) as detectioncount from entityscoring group by detectiontechnique",
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
        "sortcol":"detectioncount",
        "sortorder":"DESC"
    }
# this to return return formated results to render a widget
def render(data):
    counter = 0
    categories = []
    series = []

    for item in data:
        if counter < 10:  # Change this number to set your limit
            categories.append(item["detectiontechnique"])
            series.append(item["detectioncount"])
            counter += 1
    
    return {"series": series, "categories": categories}
