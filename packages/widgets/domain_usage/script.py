# sample name -> widgets/accounts_compromised/script.py


# this to return default widget config
def configure():
    return {
        "searchable": True,
        "datepicker": True,
        "pagination": False,
        "properties": {"type": "table"},
        "dimension": {"x": 0, "y": 9, "width": 4, "height": 4},
    }


# this to return query to be used for rendering widget and its parameters
def query():
    return {
        "query": "SELECT  source_ip as entity, source_hostname as hostname, count(*) as count from aggregation_table where source_ip is not null and source_hostname is not null and type = :type group by source_hostname,entity",
        "parameters": {"type":"hostname_entity_map"},
    }


# this to return filter queries based on filters selected by user and its parameters
def filters(filter):
    return None


# this to return free text search query and its parameters
def search(freetext):
    searchquery = ' "source_hostname" ilike :source_hostname '
    return {
        "searchquery": searchquery,
        "parameters": {"source_hostname": "%" + freetext + "%"},
    }


# this to return sort query
def sort():
    return {"sortcol": "count", "sortorder": "desc"}


def render(results):
    if not results or len(results) == 0:
        raise Exception("no results found")

    for result in results:
        result["type"] = "timelinepanel"
        result["description"] = result["hostname"]
        result["score"] = result["count"]
        result["color"] = "#02a8b5"
        result["column"]= "entity"
        result["label"]= "HostName"

        del result["hostname"]
        del result["count"]

    columns = ["entity", "score"]

    return {"result": {"columns": columns, "rows": results},"uniquekey":['entity','description'],"columnmap":["source_ip","source_hostname"]}
