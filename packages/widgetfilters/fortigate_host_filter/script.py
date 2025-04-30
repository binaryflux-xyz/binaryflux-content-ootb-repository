def query():
    return {
        "query": """SELECT DISTINCT TRIM(BOTH '"' FROM source_device_name) as host FROM aggregation_table WHERE type = :type""",
        "parameters": {"type":"host_health_status_fortigate"},
    }