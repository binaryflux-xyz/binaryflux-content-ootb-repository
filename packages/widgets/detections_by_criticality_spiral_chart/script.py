# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "spiral"},
        "dimension": {"x":8,"y":21,"width": 4, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "SELECT streamname, detectioncriticality, SUM(score) AS total_score FROM entityscoring WHERE streamname IS NOT NULL GROUP BY streamname , detectioncriticality",
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
def render(data):
    categories = set()
    crtclty = set()
    criticality = {}
    series = []
    
    for item in data:
        categories.add(item['streamname'])
        crtclty.add(item['detectioncriticality'])
    
    crtclty = list(crtclty)
    categories = list(categories)
    print(categories)
    print(crtclty)
    
    for item in data:
        if criticality.get(item['detectioncriticality']) is None :
            my_list = [0] * len(categories)
            criticality[item['detectioncriticality']] = my_list
        
        criticality[item['detectioncriticality']][categories.index(item['streamname'])] = (int(float(item['total_score'])))

    for itemkey in criticality :
        itemmap = {}
        itemmap['name'] = itemkey
        itemmap['data'] = criticality[itemkey]
        series.append(itemmap)

    return{"result":{"categories":categories,"series":series}}
