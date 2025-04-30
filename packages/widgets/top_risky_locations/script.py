# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "area","onclick":"open_offcanvaspanel"},
        "dimension": {"x":6,"y":9,"width": 6, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'SELECT source_location as country,count(*) AS count from detection where source_location is not null group by source_location',
        'parameters': {},
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


def render(result):
    data = []
    categories = []
    counter=0

    for item in result:
        if(counter<5):
            categories.append(item["country"])
            data.append(item["count"])
            counter=counter+1
        
    return {"series":[{'data':data,'name':''}], 'categories': categories,"className":"dlp-dashboardwidgets","column":"source_location","label":"Country"}
  
