# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": True,
        "properties": {"type": "semicircledonut","layout": "conciselayout"},
        "dimension": {"x": 8, "y": 12, "width":4, "height": 3} #dimensions of widget on GRID
    }

# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT detectionname AS name, COUNT(entity) AS total FROM entityscoring WHERE detectionname in ('Unauthorized Role Assignment', 'Admin privilege access granted') GROUP BY name",
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

def render(results):
    series = []
    for item in results:
        series.append({
            "key": str(item.get("name", "")),
            "count": int(item.get("total", 0))
        })

    # Define colors (adjust as needed)
    colors = [
        "#00b8d3",  # teal
        "#aed987",  # greenish
        "#eacc62",  # yellow
        "#e4604e",  # red
        "#8a6dd3"   # purple
    ]

    return {
        "result": {
            "series": series,
            "showDataLabels": True,
            "showLegends": True,
            "colors": colors[:len(series)]  # only use as many as needed
        }
    }
