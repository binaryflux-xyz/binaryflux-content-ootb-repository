# this to return default widget config
def configure():
    return {
        "searchable": False,
        "datepicker": False,
        "properties": {"type": "line", "layout": "conciselayout"},
        "dimension": {"x": 8, "y": 15, "width": 6, "height": 3}
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": """
                SELECT 
                  entity AS user,
                  COUNT(entity) AS user_count,
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
                  detectionname, entity
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
    # Fixed categories (detections)
    categories = [
        "Suspicious login attempts",
        "User Activity in High Risk Countries",
        "Multiple archived files uploaded in short period of time"
    ]

    # Prepare user data aligned with fixed categories
    user_data = {}
    for row in results:
        user = row["user"]
        count = row["user_count"]
        detection = row["detection"]

        if user not in user_data:
            user_data[user] = [0] * len(categories)

        if detection in categories:
            idx = categories.index(detection)
            user_data[user][idx] = count

    # Color palette for different users
    colors = [
        "#ff7300", "#0088fe", "#8884d8", "#82ca9d", "#ffbb28",
        "#d0ed57", "#a4de6c", "#ffc0cb", "#00c49f", "#ff8042"
    ]

    # Build series list
    series = []
    color_index = 0
    for user, counts in user_data.items():
        series.append({
            "name": user,
            "data": counts,
            "color": colors[color_index % len(colors)]
        })
        color_index += 1

    return {
        "result": {
            "categories": categories,
            "series": series
        }
    }
