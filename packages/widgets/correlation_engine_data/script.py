# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "roi_card"},
        "dimension": {"x":0,"y":8,"width": 4, "height": 2}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT 'Corelation Engine' AS stattype, COUNT(DISTINCT entity) AS total_count FROM entityscoring;",
        "parameters": {},
    }
# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None

# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort(sorcol, sortorder):
    sort += " order by " + sorcol + " " + sortorder


# this to return return formated results to render a widget
def render(results):
    return {"result":results[0]}
