# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "venn"},
        "dimension": {"x": 4, "y": 3, "width": 8, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT streamprovider as provider, COUNT(idx) AS total ,SUM(COUNT(*) FILTER (WHERE TO_TIMESTAMP(lastdetectiontime / 1000) >= NOW() - INTERVAL '24 hours'::interval)) OVER() AS last24hours,SUM(COUNT(*)) OVER() AS final_total FROM entityscoring where streamprovider IS NOT NULL GROUP BY streamprovider order by total desc;",
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
def render(results):

    categories = []
    data=[]
    last24hrsdata=[]
    total_data=[]

    for result in results:
        categories.append(result.get('total'))
        data.append(result.get('provider'))
        last24hrsdata.append(result.get('last24hours'))
        total_data.append(result.get('final_total'))
        
    return {"result":{"categories":categories,"series":data,"total":total_data,"lastoneday":last24hrsdata}}