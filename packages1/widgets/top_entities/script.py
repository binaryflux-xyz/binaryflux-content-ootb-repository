# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "bar"},
        "dimension": {"x":0,"y":11,"width": 4, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "SELECT * from fn_topoutliers",
        "parameters": {'n' : 0},
    }

# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None

# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort():
    return None

# this to return return formated results to render a widget
def render(results):

    seriesdata = []
    categoriesdata = []
    counter=0

    for item in results:
        if(counter<10):
            categoriesdata.append(item["entity"])
            seriesdata.append(item["score"])
            counter=counter+1

    return  {"series":[{'data':seriesdata}], 'categories': categoriesdata}

