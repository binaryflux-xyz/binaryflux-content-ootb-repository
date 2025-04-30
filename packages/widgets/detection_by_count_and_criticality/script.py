# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "spiral","layout":"conciselayout","onclick":"filter_apply"},
        "dimension": {"x": 8, "y": 4, "width": 4, "height": 2} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select detectionname,detectioncriticality,count(*) as detectioncount from entityscoring group by detectionname,detectioncriticality",
        "parameters": {},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):

    return None

# this to return free text search query and its parameters
def search(freetext):
    return None
  

# this to return sort query
def sort():
    return {
        "sortcol":"detectioncount",
        "sortorder":"DESC"
    }

# this to return return formated results to render a widget
def render(data):
    categories = set()
    crtclty = set()
    criticality = {}
    series = []
    
    counter = 0
    for item in data:
        if counter >= 10:
            break
        categories.add(item['detectionname'])
        crtclty.add(item['detectioncriticality'])
        counter += 1
    
    crtclty = list(crtclty)
    categories = list(categories)
    
    counter = 0
    for item in data:
        if counter >= 10:
            break
        if criticality.get(item['detectioncriticality']) is None:
            my_list = [0] * len(categories)
            criticality[item['detectioncriticality']] = my_list
        
        criticality[item['detectioncriticality']][categories.index(item['detectionname'])] = int(float(item['detectioncount']))
        counter += 1

    for itemkey in criticality:
        itemmap = {}
        itemmap['name'] = itemkey
        itemmap['data'] = criticality[itemkey]
        series.append(itemmap)

    return {"result": {"categories": categories, "series": series}}
