# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "card"},
        "dimension": {"x":0,"y":0,"width": 3, "height": 1}
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT stattype, SUM(statcount) AS total_count FROM streamx WHERE stattype = :stattype GROUP BY stattype",
        "parameters": {"stattype":"PUBLISHED"}
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
def render(data):
    return {"result":data[0]}
