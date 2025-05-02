# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "wordcloud","onclick":"not_open_offcanvaspanel","layout": "conciselayout"},
        "dimension": {"x": 8, "y": 1, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select host_name as name,count(*) as weight from aggregation_table  where host_name is not null and type = :type group by host_name",
        "parameters": {"type":"top_host_name_host_ip"},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
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

# this to return return formated results to render a widget
def render(result):
    data = []
    counter=0

    for item in result:
        if(counter<20):
            data.append(item)
            counter=counter+1
        
    return {"result":data}