
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "multichart"},
        "dimension": {"x":0,"y":2,"width": 12, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return [{
        'query': 'SELECT detectiontactic AS tactic,  COUNT(idx) AS total FROM entityscoring WHERE detectiontactic IS NOT NULL GROUP BY tactic',
        'parameters': {},
    },
  {
        'query': 'select criticality as criticality,count(*) as total from detection where criticality !=:criticality group by criticality',
        'parameters': {"criticality":'NONE'},
    },
    {
        'query': 'select detectionname as name,count(*) as total from entityscoring group by detectionname',
        'parameters': {},
    }]
 


# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    
    return None


# this to return sort query
def sort():
    return{
        "sortcol":"total",
        "sortorder":"desc"    
    }


def render(data):
    transformed_data = []
    

    for item in data[0]:
        transformed_data.append({
            "name": item["tactic"],
            "y": item["total"]
        })


  
    criticalityresult=data[1]
    counter = 0
    categories = []
    series = []

    for item in criticalityresult:
        if counter < 10:  # Change this number to set your limit
            categories.append(item["criticality"])
            series.append(item["total"])
            counter += 1


  
    detectionresult=data[2]
    seriesdata = []
    categoriesdata = []
    counter=0

    for item in detectionresult:
        if(counter<10):
            categoriesdata.append(item["name"])
            seriesdata.append(item["total"])
            counter=counter+1
    
    return {"result":{"categories":transformed_data,"criticality":{"series":series, "categories": categories},"detections":{"series":[{'data':seriesdata}], "categories": categoriesdata}}}