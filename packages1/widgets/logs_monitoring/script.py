# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "polarchart", "layout": "conciselayout"},
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
        "result": {
  "categories": ["Norway", "USA", "Germany", "Austria", "Canada"],
  "series": [
    { "name": "Gold medals", "data": [148, 113, 104, 71, 77] },
    { "name": "Silver medals", "data": [113, 122, 98, 88, 72] },
    { "name": "Bronze medals", "data": [124, 95, 65, 91, 76] }
  ]
}}