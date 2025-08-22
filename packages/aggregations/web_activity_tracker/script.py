def type() :
    return 'networkstats'

def columns() : #column names to be aggregated
    return [
                "applicationname",
                "source_ip",
                "network_bytes_transferred",
                "network_bytes_out",
                "network_bytes_in",
                "destination_port",
                "destination_ip",
                "source_hostname",
                "source_account_name"
            ]

def archive() :
    return 'monthly'