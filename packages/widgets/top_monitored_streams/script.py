# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "wordcloud"},
        "dimension": {"x":0,"y":8,"width": 6, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'SELECT streamname as name, COUNT(detectionid) AS weight FROM entityscoring GROUP BY streamname',
        'parameters': {}
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
        "sortcol":"weight",
        "sortorder":"desc"    
    }


def render(result):
    data = []
    categories = []
    counter=0

    for item in result:
        if(counter<20):
            data.append(item)
            counter=counter+1
        
    return {"result":data}
