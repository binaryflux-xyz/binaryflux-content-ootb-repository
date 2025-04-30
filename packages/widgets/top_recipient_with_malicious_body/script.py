# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "treemap","onclick":"open_offcanvaspanel"},
        "dimension": {"x":6,"y":5,"width": 6, "height": 4}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        'query': 'select distinct email_from_address as email_from_address ,count(*) as weight from detection where name=:name AND email_from_address IS NOT NULL group by email_from_address',
        'parameters': {"name":'Malicious Content in Body or Attachments'},
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
        {"column": "name", "value": 'Malicious Content in Body or Attachments', "condition": "EQ"}
      
    ]
]

    for item in data[:10]:
        transformed_data.append({
            "name": item["email_from_address"],
            "value": item["weight"]
        })

    return {"result":transformed_data,"column":"email_from_address","label":"EmailAddress","conditions":conditions,"queryType":"detection"}
  