def query():
    return {
        "query": "SELECT DISTINCT source_hostname as host FROM aggregation_table WHERE type = :type",
        "parameters": {"type":"host_health_status_linux_kaspersky"},
    }