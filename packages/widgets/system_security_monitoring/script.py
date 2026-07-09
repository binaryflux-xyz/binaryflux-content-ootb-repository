# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "table"},
        "dimension": {"x":8,"y":3,"width": 5, "height": 6}
    }


# this to return query to be used for rendering widget and its parameters
def query():

    # return {
    #     "query": "SELECT detectionname as name, 'detection' as type , detectionid as id , COUNT(DISTINCT entity) AS entities, tenant, detectiontactic, detectiontechnique, streamid FROM entityscoring WHERE detectionname IS NOT NULL GROUP BY name , id , tenant, detectiontactic, detectiontechnique, streamid ORDER BY entities DESC",
    #     "parameters": {}
    # }

    return {
        "query": "SELECT detectionname as securityconcerns, entity from entityscoring where detectionname in ('System configured insecurely', 'Security Configuration is changed', 'Disabled End to End Encryption') group by entity, detectionname",
        "parameters": {"n":0}
    }


# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return sort query
def sort():
    return None


# this to return return formated results to render a widget
def render(results):
    if not results or len(results) == 0:
        raise Exception("no results found")

    rows = []
    columns = ['Security Concerns', 'Entity']

    for result in results:
        name = result.get('securityconcerns')  
        entity = result.get('entity')
        if name and entity:
            rows.append({'Security Concerns': name, 'Entity': entity})

    return {"result": {"columns": columns, "rows": rows}}
