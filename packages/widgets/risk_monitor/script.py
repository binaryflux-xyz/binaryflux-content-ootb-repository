import json
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "multistats","layout":"backgroundchanges","widgettitle":"hidewidgettitle"},
        "dimension": {"x":0,"y":0,"width": 12, "height": 2}
    }



# this to return query to be used for rendering widget and its parameters
def query():
    return [{
        "query": "select count(DISTINCT technique) as total_count FROM detection",
        "parameters": {}
    },
           {
        "query": "SELECT SUM(statcount) AS detection_total_count FROM streamx WHERE stattype = :stattype",
        "parameters": {"stattype":"DETECTIONS"}
    },
           {
        "query": "SELECT COALESCE(SUM(statcount), 0) AS detection_todays_count FROM streamx WHERE DATE(insert_date) = CURRENT_DATE AND stattype = :stattype",
        "parameters": {"stattype":"DETECTIONS"}
    },
           {
        "query": "select COUNT(*) AS incident_total_count FROM incidentdetails",
        "parameters": {}
    },
           {
        "query": "SELECT COUNT(*) AS incident_todays_count FROM incidentdetails WHERE DATE(TO_TIMESTAMP(createdon / 1000)) = CURRENT_DATE",
        "parameters": {}
    },
           {
        "query": "SELECT SUM(statcount) AS total_event_count FROM streamx WHERE stattype = :stattype",
        "parameters": {"stattype":"PUBLISHED"}
    },
           {
        "query": "SELECT COALESCE(SUM(statcount), 0) AS todays_event_count FROM streamx WHERE DATE(insert_date) = CURRENT_DATE AND stattype = :stattype",
        "parameters": {"stattype":"PUBLISHED"}
    },
           {
        "query": "select * from implicit_algorithm",
        "parameters": {}
    },
           {
        "query": "select * from implicit_listallcollectors",
        "parameters": {}
    }]

def algorithm():
    payload = {}
    return rest.internalCall("POST","/collector/listallactivenodes",payload)

def listallcollectors():
    payload = {
      "tenant":"cisco"
    }
    return rest.internalCall("POST","/collector/listallcollectors",payload)

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
    present_count = int(data[0][0]["total_count"])  # ensure it's an integer
    coverage = round((float(present_count) / TOTAL_TECHNIQUES) * 100, 2)
    threatcoverage = [{"total_threatcoverage": str(coverage) + "%"}]

    activedatasource = data[7]

    # Sum all 'currenteps' values (if present)
    eps_count = sum(item.get('currenteps', 0) for item in activedatasource)

    colltectorlist = json.loads(data[8])
    colltectorcount = len(colltectorlist)
    
    return {"result":{"total_threatcoverage":threatcoverage,"threat_name": "Threat Coverage",
    "detection_total_count":data[1][0],"detection_todays_count":data[2][0],"detection_name":"Total Detections",
    "incident_total_count":data[3][0],"incident_todays_count":data[4][0],"incident_name":"Total Incidents",
    "total_event_count":data[5][0],"todays_event_count":data[6][0],"event_name":"Total Events",
    "total_eps_count":eps_count,"total_datasource":colltectorcount,"data_source_name":"Total Source"}}