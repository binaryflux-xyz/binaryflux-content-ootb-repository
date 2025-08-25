# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "roi_card"},
        "dimension": {"x":0,"y":6,"width": 4, "height": 2}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT 'AUTOMATIONS' AS stattype,(SUM(CASE WHEN stattype = :statype_automation THEN statcount ELSE 0 END) /SUM(CASE WHEN stattype = :statype_detection THEN statcount ELSE 0 END) * 100) AS total_count FROM streamx WHERE stattype = :statype_detection OR stattype = :statype_automation;",
        "parameters": {"statype_detection":"DETECTIONS","statype_automation":"AUTOMATIONS"},
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
        
    return {"result":results[0]}
