# Sample name -> widgets/accounts_compromised/script.py

# This returns the default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "pagination": False,
        "properties": {"type": "line","onclick":"open_offcanvaspanel"},
        "dimension": {"x": 0, "y": 13, "width": 4, "height": 4}
    }

# This returns the query to be used for rendering the widget and its parameters
def query():
    return {
        'query': '''
            SELECT DISTINCT email_from_address, email_attachments_size 
            FROM detection 
            WHERE name = :name 
                AND email_from_address IS NOT NULL 
            GROUP BY email_from_address, email_attachments_size
        ''',
        'parameters': {"name": 'Excessive Attachment Size Limit Exceeded'},
    }

# This returns filter queries based on filters selected by the user and its parameters
def filters(filter):
    return None

# This returns free text search query and its parameters
def search(freetext):
    return None

# This returns the sort query
def sort():
    return {
        "sortcol": "email_attachments_size",
        "sortorder": "desc"
    }

  
# This processes and renders the widget results
def render(results):
    if not results or len(results) == 0:
        raise Exception("No results found")

    series = []
    data = []
    categories = []
    counter = 0

    for result in results:
        if counter < 5:
            categories.append(result["email_from_address"])
            data.append(round(int(result['email_attachments_size']) / (1024.0 * 1024 * 1024), 2))
            counter += 1

    series_obj = {
        "name": "",
        "data": data,
        "color": "#ff7300"
    }

    conditions = [
    [
        {"column": "name", "value": "Excessive Attachment Size Limit Exceeded", "condition": "EQ"}
      
    ]
]

    series.append(series_obj)

    return {"result": {"categories": categories, "series": series},"className":"dlp-dashboardwidgets","unit":"Gb","column":"email_from_address","label":"EmailAddress","conditions":conditions,"queryType":"detection"}
