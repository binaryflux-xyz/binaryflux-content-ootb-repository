# this to return default widget config
def configure():
    return {
        "searchable": True, #Boolean value depending whether the widget is searchable or not
        "properties": {"type": "type_of_widget"},
        "filters": ["filter-1", "filter-2"],
        "dimension": {"x": 0, "y": 0, "width": 4, "height": 6} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select * from table_name where condition like :condition",
        "parameters": {"condition": "%H%"},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    filterqueries = []
    parameters = {}
    if filters:
        if filters["filter-1"]:
            filterqueries.append("  streamid in (:streams) ")
            parameters["streams"] = filters["stream"]

        if filters["filter-2"]:
            filterqueries.append(" department in (:departments) ")
            parameters["department"] = filters["department"]

    return {"filterqueries": filterqueries, "parameters": parameters}

# this to return free text search query and its parameters
def search(freetext):
    searchquery = " accountname like :accountname "
    return {
        "searchquery": searchquery,
        "parameters": {"accountname": "%" + freetext + "%"},
    }

# this to return sort query
def sort(sorcol, sortorder):
    return None

# this to return return formated results to render a widget
def render(results):
    return None