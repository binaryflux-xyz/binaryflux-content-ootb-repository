# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "overview_statcard","layout":"card"},
        "dimension": {"x":0,"y":0,"width": 3, "height": 1}
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select count(DISTINCT technique) as total_count FROM detection;",
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
    TOTAL_TECHNIQUES = 196
    present_count = int(data[0]["total_count"])  # ensure it's an integer
    coverage = round((float(present_count) / TOTAL_TECHNIQUES) * 100, 2)
    result = [{"total_threatcoverage": str(coverage) + "%"}]

    return {"result":{"total_threatcoverage":result,"name": "Threat Coverage"}}
