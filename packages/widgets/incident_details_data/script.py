# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "incident_list"},
        "dimension": {"x": 4, "y": 8, "width": 8, "height": 2} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select name,criticality ,assignee ,status ,createdby ,createdon  from incidentdetails",
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
    if not results or len(results) == 0:
        raise Exception("no results found")

    
    return {"result":results}
