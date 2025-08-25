# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "line"},
        "dimension": {"x":0,"y":0,"width": 6, "height": 3},
        "icon":"Cribl"
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT DATE(insert_date) AS insertdate, COUNT(score) AS value FROM entityscoring where streamname = :streamname GROUP BY insertdate ORDER BY insertdate ASC",
        "parameters": {"streamname":"Suspicious Logon Attempts"}
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

    results = sorted(results, key=lambda x: x["insertdate"])
    
    if not results or len(results) == 0:
        raise Exception("no results found")
    
    categories=[]
    data=[]
    series=[]

    for result in results :
        categories.append(result.get('insertdate'))
        data.append(result.get('value'))
    
    seriesObj={
        "name":"detections",
        "data":data,
        "color":"#ff7300"
    }

    series.append(seriesObj)
    
    return {"result":{"categories":categories,"series":series}}
