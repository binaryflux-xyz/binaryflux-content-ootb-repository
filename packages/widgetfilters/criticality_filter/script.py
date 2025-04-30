# sample name -> widgetfilters/criticality_filter/script.py

def query():
    return {
        "query": "SELECT DISTINCT detectioncriticality FROM entityscoring WHERE detectioncriticality IS NOT NULL",
        "parameters": {},
    }