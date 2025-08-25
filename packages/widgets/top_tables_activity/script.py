def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "wordcloud","layout": "conciselayout","onclick":"not_open_offcanvaspanel"},
        "dimension": {"x":0,"y":4,"width": 4, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select distinct table_name as name,count(*)as weight from aggregation_table where table_name is not null and type=:type group by table_name',
        'parameters': {"type":"injection_topoperation_data"}
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
        if(counter<10):
            data.append(item)
            counter=counter+1
        
    return {"result":data}