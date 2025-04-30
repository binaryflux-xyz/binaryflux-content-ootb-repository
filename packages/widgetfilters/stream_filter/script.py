# sample name -> widgetfilters/criticality_filter/script.py

def query():
    return {
        "query": "SELECT DISTINCT streamname FROM entityscoring WHERE streamname IS NOT NULL",
        "parameters": {}
    }