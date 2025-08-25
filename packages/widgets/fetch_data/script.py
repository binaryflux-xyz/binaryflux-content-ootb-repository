# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "area","layout": "conciselayout"},
        "dimension": {"x":9,"y":0,"width": 3, "height": 2}
    }

def query():
    return {
        'query': 
            "SELECT user_name AS name,COUNT(*) AS count,STRFTIME(TO_TIMESTAMP(timestamp / 1000), '%m-%d:%H') AS xaxis FROM aggregation_table WHERE type = :type AND operation = :operation GROUP BY user_name, xaxis",
        'parameters': {"type": "database_crud_data", "operation": "SELECT"}
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
  
    # Step 1: Extract unique x-axis values (categories) and sort them
    categories = sorted({item['xaxis'] for item in result})

    # Step 2: Initialize a dictionary to hold series data
    series_map = {item['name']: [0] * len(categories) for item in result}

    # Step 3: Populate the series_map with actual counts
    for item in result:
      index = categories.index(item['xaxis'])
      series_map[item['name']][index] = item['count']

    # Step 4: Convert series_map into the desired list of dictionaries format
    series = [{'name': name, 'data': counts} for name, counts in series_map.items()]

    colors = ["#09d37a","#499071","#079a5a","#00876c"]
        
    return {"series":series,'categories': categories,"colors":colors}