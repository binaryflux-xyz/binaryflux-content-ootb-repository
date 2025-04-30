def type() :
    return 'host_detection_map'

def columns() : #column names to be aggregated
    return ['source_hostname']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('source_hostname')