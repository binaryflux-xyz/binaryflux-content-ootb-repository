import json
# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "line"},
        "dimension": {"x": 4, "y": 11, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return [
      {
        "query": "select * from implicit_algorithm",
        "parameters": {}
    },
           {
        "query": "select * from implicit_listallcollectors",
        "parameters": {}
    }
    ]
  
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
    activedatasource = data[0]
    collectorlist = json.loads(data[1])

    # Build a lookup for provider -> currenteps
    eps_lookup = {ds['provider']: ds.get('currenteps', 0) for ds in activedatasource}

    categories = []
    eps_count = []

    for collector in collectorlist:
        name = collector.get("name", "")
        provider = collector.get("log.provider", "")
        categories.append(name)

        # Match provider with activedatasource
        current_eps = eps_lookup.get(provider, 0)
        eps_count.append(current_eps)

    series = [
        {
            "name": "EPS",
            "data": eps_count,
            "color": "#ff7300"
        }
    ]

    return {"result":{"series": series,"categories": categories}}
