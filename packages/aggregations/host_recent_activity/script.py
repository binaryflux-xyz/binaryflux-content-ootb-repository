def type() :
    return 'host_health_status'

def columns() : #column names to be aggregated
    return ['host']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('host')