# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "overview_statcard","layout":"card"},
        "dimension": {"x":6,"y":0,"width": 3, "height": 1}
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return [{
        "query": "select COUNT(*) AS total_count FROM incidentdetails",
        "parameters": {}
    },
           {
        "query": "SELECT COUNT(*) AS todays_count FROM incidentdetails WHERE DATE(TO_TIMESTAMP(createdon / 1000)) = CURRENT_DATE",
        "parameters": {}
    }]


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
    
    return {"result":{"total_count":data[0],"todays_count":data[1],"name":"Total Incidents"}}