# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "donut"},
        "dimension": {"x":0,"y":5,"width": 4, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select count(*) as count,risk from genaianalysis where agent=:agent and risk is not null group by risk',
        'parameters': {"agent":"email-pii"},
    }


# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    return None


# this to return sort query
def sort():
    return{
        "sortcol":"count",
        "sortorder":"desc"    
    }


def render(results):
    series = {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "CRITICAL": 0, "NONE": 0}

    for item in results:
        risk_level = item["risk"].upper()
        if risk_level in series:
            series[risk_level] += item["count"]

    return {"result": series,"className":"dlp-dashboardwidgets"}