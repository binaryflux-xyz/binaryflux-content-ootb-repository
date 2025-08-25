# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "overview_statcard","layout":"card"},
        "dimension": {"x":3,"y":0,"width": 3, "height": 1}
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return [{
        "query": "SELECT SUM(statcount) AS total_count FROM streamx WHERE stattype = :stattype",
        "parameters": {"stattype":"DETECTIONS"}
    },
           {
        "query": "SELECT SUM(statcount) AS todays_count FROM streamx WHERE DATE(insert_date) = CURRENT_DATE AND stattype = :stattype",
        "parameters": {"stattype":"DETECTIONS"}
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
    
    return {"result":{"total_count":data[0],"todays_count":data[1],"name":"Total Detections"}}