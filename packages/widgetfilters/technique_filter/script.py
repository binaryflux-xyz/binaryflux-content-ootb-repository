# sample name -> widgetfilters/criticality_filter/script.py

def query():
    return {
        "query": "SELECT DISTINCT detectiontechnique FROM entityscoring WHERE detectiontechnique IS NOT NULL",
        "parameters": {},
    }