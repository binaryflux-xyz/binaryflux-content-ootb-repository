# sample name -> widgets/accounts_compromised/script.py
import time

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "sankey","limit":5,"onclick":"open_offcanvaspanel"},
        "dimension": {"x":0,"y":6,"width": 6, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": """
            SELECT source_ip as sourceip, destination_ip as destinationip, 
                   SUM(CASE 
                          WHEN network_bytes_transferred ~ '^[0-9]+$' THEN CAST(network_bytes_transferred AS NUMERIC) 
                          ELSE 0 
                       END) as total_bytes 
            FROM detection 
            WHERE source_ip is not null 
              AND destination_ip is not null 
              AND network_bytes_transferred is not null 
            GROUP BY source_ip, destination_ip;
        """,
        "parameters": {"n": 0}
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
        "sortcol":"total_bytes",
        "sortorder":"desc"    
    }


# this to return return formated results to render a widget
def render(results):
    
    if not results or len(results) == 0:
        raise Exception("no results found")
    categories = []

    counter=0
            
    for result in results:
        
        source_ip = result["sourceip"]
        destination_ip = result["destinationip"]
        bytes_transferred = int(result['total_bytes'])
        if(counter<10):
            categories.append([source_ip, destination_ip, round(bytes_transferred / (1024.0 * 1024 * 1024), 2)  ])
            counter=counter+1

    
    columns = ['from','to','weight']

    return  {"series":[{"keys": columns, "data": categories}],"column":"source_ip","label":"Sourceip"}
