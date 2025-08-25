# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "critical"},
        "dimension": {"x": 4, "y": 6, "width": 8, "height": 2} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT detectionname,detectioncriticality,COUNT(*) AS count_per_detection, SUM(COUNT(*) FILTER (WHERE TO_TIMESTAMP(lastdetectiontime / 1000) >= NOW() - INTERVAL '24 hours'::interval)) OVER() AS last24hours,SUM(COUNT(*)) OVER() AS total FROM entityscoring WHERE detectioncriticality = :detectioncriticality GROUP BY detectionname, detectioncriticality ORDER BY count_per_detection DESC",
        "parameters": {"detectioncriticality": "HIGH"},
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
