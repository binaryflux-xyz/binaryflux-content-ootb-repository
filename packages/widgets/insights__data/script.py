# this to return default widget config
def configure():
    return {
        "searchable": False, #Boolean value depending whether the widget is searchable or not
        "datepicker": False,
        "properties": {"type": "area"},
        "dimension": {"x": 4, "y": 0, "width": 8, "height": 3} #dimensions of widget on GRID
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT stattype, SUM(statcount) AS cumulative_sum, DATE(insert_date) AS publish_date FROM streamx WHERE objecttype = 'stream' AND insert_date >= insert_date GROUP BY stattype,publish_date ORDER BY publish_date;",
        "parameters": {}
    }
 
# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None
# this to return free text search query and its parameters
def search(freetext):
    return None

# this to return sort query
def sort(sorcol, sortorder):
    sort += " order by " + sorcol + " " + sortorder

# this to return return formated results to render a widget
def render(results):
    results = sorted(results, key=lambda x: x["publish_date"])

    categories = []
    published_data = []
    filtered_data = []
    detection_data=[]
    automation_data=[]
    series = []
    published_sum = 0

    for result in results:
        
        date = result.get('publish_date') 
        if date not in categories: 
                categories.append(date)
        if result["stattype"] == "PUBLISHED":
            published_data.append(result["cumulative_sum"])
            published_sum += result["cumulative_sum"]
        elif result["stattype"] == "FILTERED":
            filtered_data.append(result["cumulative_sum"])
        elif result["stattype"] == "DETECTIONS":
            detection_data.append(result["cumulative_sum"])
        elif result["stattype"] == "AUTOMATIONS":
            automation_data.append(result["cumulative_sum"])
    
    series.append({"name": "PUBLISHED","color":'#00876c', "data": published_data})
    series.append({"name": "FILTERED","color":'#63b179', "data": filtered_data})
    series.append({"name": "DETECTIONS","color":'#88c580', "data": detection_data})
    series.append({"name": "AUTOMATIONS","color":'#aed987', "data": automation_data})
    
    return {"result":{"categories":categories,"series":series,"published_sum":published_sum}}

           