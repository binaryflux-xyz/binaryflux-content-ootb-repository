# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "semicircledonut", "layout": "conciselayout"},
        "dimension": {"x": 8, "y": 21, "width": 4, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": """
            SELECT 
                COUNT(DISTINCT entity) AS user_count, 
                detectionname AS detection
            FROM 
                entityscoring 
            WHERE 
                detectionid IN (
                    '6511f309f47d8e39b9cdb4b7', 
                    '65e0ba55b233eb2da3d02cb3', 
                    '65f9393d9028f678cacb64df'
                )
            GROUP BY 
                detectionname
            ORDER BY 
                user_count DESC;
        """,
        "parameters": {'n': 0},
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


def render(results):
    return {
        "result": {"series":[
        {
            "key": "CRITICAL",
            "count": 2
        },
        {
            "key": "HIGH",
            "count": 1
        },
        {
            "key": "MEDIUM",
            "count": 1
        }
    ]}}