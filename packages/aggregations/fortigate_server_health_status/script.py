def type() :
    return 'host_health_status_fortigate'

def columns() : #column names to be aggregated
    return ['source_device_name']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('source_device_name')