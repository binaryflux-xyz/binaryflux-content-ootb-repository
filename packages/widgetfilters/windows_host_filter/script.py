def query():
    return {
        "query": "SELECT DISTINCT host as host FROM aggregation_table WHERE type = :type",
        "parameters": {"type":"host_health_status"},
    }