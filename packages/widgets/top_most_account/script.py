# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "wordcloud"},
        "dimension": {"x":8,"y":0,"width": 4, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select source_account_name as name, count (*) as weight from detection where source_account_name is not null group by source_account_name',
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
        
    return {"result":data,"column":"source_account_name","label":"Accoutname","uniquekey":['name'],"columnmap":["source_account_name"]}
