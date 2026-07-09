# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "treemap"},
        "dimension": {"x":8,"y":8,"width": 4, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "SELECT detectiontechnique AS technique,  COUNT(idx) AS total FROM entityscoring WHERE detectiontechnique IS NOT NULL GROUP BY technique",
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
    sort += " order by " + sorcol + " " + sortorder


# this to return return formated results to render a widget
def render(data):
    transformed_data = []

    for item in data:
        transformed_data.append({
            "name": item["technique"],
            "value": item["total"]
        })
    
    return {"result":transformed_data}
