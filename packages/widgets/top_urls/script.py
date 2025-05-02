# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "treemap","layout": "conciselayout"},
        "dimension": {"x": 4, "y": 4, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "select url as name,count(*) as value from aggregation_table  where url is not null and type = :type group by url",
        "parameters": {"type":"top_urls_data"},
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
        "sortcol":"value",
        "sortorder":"desc"    
    }


def render(results):
    if not results:
        raise Exception("no results found")
    
    # Limit to the first 10 records if there are more than 10
    if len(results) > 10:
        results = results[:10]
    
    return {"result": results}


