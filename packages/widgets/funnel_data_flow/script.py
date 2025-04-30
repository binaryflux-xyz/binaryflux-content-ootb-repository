# sample name -> widgets/accounts_compromised/script.py


# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "funnel","layout": "conciselayout"},
        "dimension": {"x": 4, "y": 6, "width": 4, "height": 2}
    }



# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "select stattype ,sum(statcount) as statcount from streamx  group by stattype;",
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
    return None



def render(results):
    # Define the allowed stattypes and their desired order
    allowed_stattypes = ['PUBLISHED','FILTERED','DETECTIONS']

    # Filter and transform the results into the desired format
    filtered_data = [
        [item['stattype'], item['statcount']]
        for item in results
        if item['stattype'] in allowed_stattypes
    ]

    # Sort the transformed data according to the defined order
    transformed_data = sorted(
        filtered_data,
        key=lambda x: allowed_stattypes.index(x[0])
    )

    return {"result": transformed_data}


