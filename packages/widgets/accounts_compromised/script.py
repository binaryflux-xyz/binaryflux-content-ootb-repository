# sample name -> widgets/accounts_compromised/script.py


# this to return default widget config
def configure():
    return {
        "searchable": True,
        "properties": {"type": "table"},
        "filters": ["stream", "department"],
        "dimension": {"x": 0, "y": 0, "width": 4, "height": 6}
    }


# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "select user.email , score from detection where criticality like :criticality",
        "parameters": {"criticality": "%H%"},
    }


# this to return filter queries based on filters selected by user and its parameters
def filters(filters):

    filterqueries = []
    parameters = {}
    if filters:
        if filters["stream"]:
            filterqueries.append("  streamid in (:streams) ")
            parameters["streams"] = filters["stream"]

        if filters["department"]:
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
    sort += " order by " + sorcol + " " + sortorder


# this to return return formated results to render a widget
def render(results):

    if not results or len(results) == 0:
        raise Exception("no results found")
    
    rows = []
    columns = ['user.email' , 'score']


    for resultobj in results:
        rows.append([resultobj.get("user.email"), resultobj.get('score')])

    return  {"result":{"columns": columns, "rows": rows}}