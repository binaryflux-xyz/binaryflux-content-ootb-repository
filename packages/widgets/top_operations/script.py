# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "stackedbar","layout": "conciselayout"},
        "dimension": {"x":4,"y":2,"width": 4, "height": 2}
    }

def query():
    return {
        'query': 
            "select table_name,operation,count(*) as count from aggregation_table where operation IS NOT NULL AND type=:type group by operation,table_name;",
        'parameters': {"type": "injection_topoperation_data"}
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
    categories = sorted({item['operation'] for item in result})

    # Step 2: Initialize a dictionary to hold series data
    series_map = {item['table_name']: [0] * len(categories) for item in result}

    # Step 3: Populate the series_map with actual counts
    for item in result:
      index = categories.index(item['operation'])
      series_map[item['table_name']][index] = item['count']

    # Step 4: Convert series_map into the desired list of dictionaries format
    series = [{'name': name, 'data': counts} for name, counts in series_map.items()]
        
    return {"series":series,'categories': categories}