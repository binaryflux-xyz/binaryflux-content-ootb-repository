# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "wordcloud"},
        "dimension": {"x":0,"y":1,"width": 4, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select distinct email_from_address as email_from_address ,count(*) as weight from detection where name=:name AND email_from_address IS NOT NULL group by email_from_address',
        'parameters': {"name":'Suspicious Email Headers'},
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
        "sortcol":"weight",
        "sortorder":"desc"    
    }


def render(data):
    transformed_data = []

    conditions = [
    [
        {"column": "name", "value": "Suspicious Email Headers", "condition": "EQ"}
      
    ]
]

    for item in data[:20]:  # Limit to first 20 records
        transformed_data.append({
            "name": item["email_from_address"],
            "weight": item["weight"]
        })
    
    return {"result": transformed_data,"column":"email_from_address","label":"EmailAddress","conditions":conditions,"queryType":"detection"}
