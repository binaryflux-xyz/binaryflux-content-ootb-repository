# sample name -> widgets/accounts_compromised/script.py
import time

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "sankey","onclick":"open_offcanvaspanel"},
        "dimension": {"x":0,"y":9,"width": 6, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": """
            SELECT email_from_address, email_to_address , 
                   SUM(email_attachments_size) as total_bytes 
            FROM aggregation_table 
            WHERE email_from_address is not null 
              AND email_to_address is not null 
              AND email_attachments_size is not null 
              and email_attachments_size !=0 
              AND type = :type
            GROUP BY email_from_address, email_to_address;
        """,
        "parameters": {"type":"microsoft_attachments_exchanged"}
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
        
        source_ip = result["email_from_address"]
        destination_ip = result["email_to_address"]
        bytes_transferred = int(result['total_bytes'])
        if(counter<10):
            categories.append([source_ip, destination_ip, round(bytes_transferred / (1024.0 * 1024 * 1024), 2)  ])
            counter=counter+1

    
    columns = ['from','to','weight']
    
    return  {"series":[{"keys": columns, "data": categories}],"column":"email_from_address","label":"EmailAddress","uniquekey":["from","to"],"columnmap":["email_from_address","email_to_address"]}