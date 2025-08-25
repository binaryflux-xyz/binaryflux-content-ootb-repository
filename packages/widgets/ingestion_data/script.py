# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "roi_table"},
        "dimension": {"x": 0, "y": 0, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT * from fn_datasource_widget limit 5",
        "parameters": {"n":0,'stattype':"PUBLISHED",'requiredepoch':'true'},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None

# this to return free text search query and its parameters
def search(freetext):
    searchquery = " accountname like :accountname "
    return {
        "searchquery": searchquery,
        "parameters": {"accountname": "%" + freetext + "%"},
    }

# this to return sort query
def sort(sorcol, sortorder):
    sort += " order by " + sorcol + " " + sortorder

# this to return return formated results to render a widget
def render(results):
    if not results or len(results) == 0:
        raise Exception("no results found")

    rows = []
    columns = ['provider', 'total']

    return {"result": {"columns": columns, "rows": results}}
