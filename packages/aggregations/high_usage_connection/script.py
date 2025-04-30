def type() :
    return 'entity_bandwidth_map'

def columns() : #column names to be aggregated
    return ['source_ip' , 'network_bytes_transferred']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('source_ip')