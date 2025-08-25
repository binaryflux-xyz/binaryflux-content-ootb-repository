# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "fatalwidget","layout": "conciselayout"},
        "dimension": {"x": 0, "y": 0, "width": 12, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": """
            SELECT 
                streamprovider AS provider,
                entity AS user,
                name AS detection,
                context AS alerts,
                criticality AS criticality
            FROM 
                detection
            WHERE 
                streamprovider IS NOT NULL
                AND entity IS NOT NULL
                AND name IS NOT NULL
                AND context IS NOT NULL
                AND criticality IS NOT NULL
                And name in ('Abnormal Amount Data Transmitted for destination port outside the CIDR range - Firewall')
            GROUP BY 
                streamprovider, entity, name, context, criticality, insert_date
            Order By
                insert_date DESC
            LIMIT 10
        """,
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


# this to return return formated results to render a widget
def render(results):
    if len(results) > 10:
        results = results[:10]  # Limit to the first five records        
    columnList=['provider', 'user', 'detection','alerts', 'criticality'];
    
    return {"result": results,"columns":columnList}