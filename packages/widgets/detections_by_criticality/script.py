# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "pie","onclick":"open_offcanvaspanel"},
        "dimension": {"x":8,"y":0,"width": 4, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "select criticality, count(*) as total from detection group by criticality",
        "parameters": {}
    }


# this to return filter queries based on filters selected by user and its parameters
def filters(filters):

    return None


# this to return free text search query and its parameters
def search(freetext):
    return None


# this to return sort query
def sort():
    return None


# this to return return formated results to render a widget
def render(data):
    transformed_data = []

    for item in data[:20]:
        transformed_data.append({
            "name": item["criticality"],
            "y": item["total"]
        })
    
    return {"result":transformed_data,"column":"criticality","label":"Criticality"}