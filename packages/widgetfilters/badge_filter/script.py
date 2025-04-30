# sample name -> widgetfilters/criticality_filter/script.py

def query():
    return {
        "query": "SELECT DISTINCT id as badge,name FROM badge",
        "parameters": {}
    }
