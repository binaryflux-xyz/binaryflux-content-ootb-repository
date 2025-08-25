# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "fatalwidget","layout": "conciselayout"},
        "dimension": {"x": 0, "y": 9, "width": 12, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": """
            SELECT 
                name AS detection,
                context AS alerts,
                criticality AS criticality
            FROM 
                detection
            WHERE 
                name IS NOT NULL
                AND context IS NOT NULL
                AND detectionid IS NOT NULL
                AND criticality IS NOT NULL
                AND detectionid IN ('65f9397e9028f678cacb6560', '650ea3cc29ac672df96da233')
            GROUP BY 
                name, context, detectionid, insert_date, criticality
            ORDER BY
                insert_date DESC
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
    columnList=['criticality', 'detection', 'alerts'];
    
    return {"result": results,"columns":columnList}