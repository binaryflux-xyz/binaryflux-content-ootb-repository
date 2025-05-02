# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "bar","layout": "conciselayout"},
        "dimension": {"x": 0, "y": 7, "width": 4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT category_name  as categoryname, category_source as categorysource ,count(*) as total from aggregation_table where category_name is not null and type = :type group by category_name,category_source",
        "parameters": {"type":"top_category_name"},
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
        "sortcol":"total",
        "sortorder":"desc"    
    }


def render(result):
    data = []
    categories = []
    counter = 0

    for item in result:
        if counter < 10:
            # Append the total value to the data list
            data.append(item["total"])
            # Append the concatenated category to the categories list
            categories.append(item["categoryname"] + "(" + item["categorysource"] + ")")
            counter += 1

    return {"series": [{'data': data}], 'categories': categories}