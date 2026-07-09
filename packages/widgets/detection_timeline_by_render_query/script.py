# sample name -> widgets/accounts_compromised/script.py

# this to return default widget config

import time

def configure():
    return {
        "searchable": False,
        "datepicker": True,
        "properties": {"type": "bubble"},
        "dimension": {"x":0,"y":11,"width": 6, "height": 3}
    }


# this to return query to be used for rendering widget and its parameters
def query():

    return {
        "query": "SELECT DATE(insert_date) AS insertdate, COUNT(score) AS yaxis, SUM(score) AS size FROM entityscoring GROUP BY insertdate",
        "parameters": {}
    }


# this to return filter queries based on filters selected by user and its parameters
def filters(filters):

    filterqueries = []
    parameters = {}
    if filters:
        if filters["stream"]:
            filterqueries.append("  streamid in (:streams) ")
            parameters["streams"] = filters["stream"]

        if filters["department"]:
            filterqueries.append(" department in (:departments) ")
            parameters["department"] = filters["department"]

    return {"filterqueries": filterqueries, "parameters": parameters}


# this to return free text search query and its parameters
def search(freetext):
    searchquery = " accountname ilike :accountname "
    return {
        "searchquery": searchquery,
        "parameters": {"accountname": "%" + freetext + "%"},
    }


# this to return sort query
def sort(sorcol, sortorder):
    sort += " order by " + sorcol + " " + sortorder


# this to return return formated results to render a widget
def render(results):

    if not results or len(results) == 0:
        raise Exception("no results found")

    converted_data = []

    sorted_data = sorted(results, key=lambda x: int(float(x["size"])))
    n = len(results)
    q1_index = int(n/3)
    q3_index = int((2*n)/3)

    q1 = int(float(sorted_data[q1_index]["size"]))
    q3 = int(float(sorted_data[q3_index]["size"]))

    for result in results:
        insertdate = int(time.mktime(time.strptime(result["insertdate"], "%Y-%m-%d"))) * 1000
        size = int(float(result["size"]))
        converted_entry = { "x":insertdate,
                            "y":result["yaxis"],
                            "z":size,
                            "zlabel": "RiskScore",
                            "xlabel": "DateTime",
                            "ylabel": "Frequency",
                            "color": "#FF0000" if size > q3 else "#FFA500" if size > q1 else "#008000"}
        converted_data.append(converted_entry)

    return {"result":converted_data}
