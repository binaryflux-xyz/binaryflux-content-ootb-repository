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
                   SUM(network_bytes_transferred) as total_bytes 
            FROM aggregation_table 
            WHERE source_ip is not null 
              AND destination_ip is not null 
              AND network_bytes_transferred is not null 
              AND type = :type
            GROUP BY source_ip, destination_ip;
        """,
        "parameters": {"type":"source_destination_data_transfer"}
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

    return  {"series":[{"keys": columns, "data": categories}],"column":"source_ip","label":"SourceIP","uniquekey":["from","to"],"columnmap":["source_ip","destination_ip"]}
