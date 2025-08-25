# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "column"},
        "dimension": {"x":0,"y":12,"width": 6, "height": 3},
        "icon":"Microsoft"
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT DATE(insert_date) AS insertdate,detectioncriticality , COUNT(score) AS value FROM entityscoring where streamname =:streamname GROUP BY insertdate,detectioncriticality ORDER BY insertdate asc",
        "parameters": {"streamname":"Failed Patented Docs. Access Attempt"}
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
# def render(results):

#     results = sorted(results, key=lambda x: x["insertdate"])
    
#     if not results or len(results) == 0:
#         raise Exception("no results found")
    
#     categories=[]
#     data=[]
#     series=[]
#     criticality=[]

#     for result in results :
#         categories.append(result.get('insertdate'))
#         data.append(result.get('value'))
#         criticality.append(result.get('detectioncriticality'))
#     seriesObj={
#         "name":"detections",
#         "data":data,
#         "color":"#ff7300"
#     }

#     series.append(seriesObj)
    
#     return {"result":{"categories":categories,"series":series}}

def render(results):
    results = sorted(results, key=lambda x: x["insertdate"])
    
    if not results or len(results) == 0:
        raise Exception("no results found")
    
    series = []

    for result in results:
        formatted_result = {
            "insert_date": result.get('insertdate'),
            "detectioncriticality": result.get('detectioncriticality'),
            "value": result.get('value')
        }
        series.append(formatted_result)

    return {"result": series}

