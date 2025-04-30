
def query():
    return {
        "query": "SELECT DISTINCT detectionname FROM entityscoring WHERE detectionname IS NOT NULL",
        "parameters": {}
    }