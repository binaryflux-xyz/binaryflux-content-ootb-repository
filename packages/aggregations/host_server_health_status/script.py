def type() :
    return 'host_health_status_linux_kaspersky'

def columns() : #column names to be aggregated
    return ['source_hostname']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('source_hostname')