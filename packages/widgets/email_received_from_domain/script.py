
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "bar" ,"onclick":"open_offcanvaspanel"},
        "dimension": {"x":4,"y":1,"width": 4, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "SELECT DISTINCT email_from_domain as domain, COUNT(*) AS score FROM aggregation_table WHERE email_from_domain IS NOT NULL and type = :type GROUP BY email_from_domain",
        "parameters": {"type":"top_domain_microsoft_events"}
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
        "sortcol":"score",
        "sortorder":"desc"    
    }


def render(result):
    data = []
    categories = []
    counter=0

    for item in result:
        if(counter<10):
            categories.append(item["domain"])
            data.append(item["score"])
            counter=counter+1
        
    return {"series":[{'data':data}], 'categories': categories,"column":"email_from_domain","label":"EmailAddress","type":"top_domain_microsoft_events","uniquekey":["category"],"columnmap":["email_from_domain"]}