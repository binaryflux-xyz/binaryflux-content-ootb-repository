# sample name -> widgets/accounts_compromised/script.py
# this to return default widget config
def configure():
    return {
        "searchable": False,
        "properties": {"type": "statcard","layout":"card","graphtype":"bar"},
        "dimension": {"x": 3, "y": 0, "width": 3, "height": 1} #dimensions of widget on GRID
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return[{
  "query": "SELECT distinct host ,  count(*) as total FROM aggregation_table WHERE  type = :type group by host order by total desc limit 2;",
  "parameters": {
    "type": "tenant_health_monitor_breakdown"
  }
},
          {
  "query": "SELECT count(distinct host) as hosts FROM aggregation_table WHERE  type = :type;",
  "parameters": {
    "type": "tenant_health_monitor_breakdown"
  }
}]


# this to return filter queries based on filters selected by user and its parameters
def filters(filters):
    return None


# this to return free text search query and its parameters
def search(freetext):
    return None


# this to return sort query
def sort(sorcol, sortorder):
    return None



def render(results):
    data=results[0]

    categories = [item["host"] for item in data]
    series = [item["total"] for item in data]

    return {"result": {"series": [{'data': series, "name": 'Devices'}], "categories": categories, "total": results[1][0].get("hosts"),"colors":["#23483b"],"className":"security-control-dashboardstats"}}
    
    # return {"result":results}
