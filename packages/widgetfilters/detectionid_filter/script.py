
def query():
    return {
        "query": "SELECT DISTINCT detectionid FROM entityscoring WHERE detectionid IS NOT NULL",
        "parameters": {}
    }