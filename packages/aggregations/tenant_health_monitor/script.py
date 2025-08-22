def type() :
    return 'tenant_health_monitor_breakdown'


def columns() : #column names to be aggregated
    return ['provider','host']

def archive() :
    return 'weekly'
  

def uniquekey(message):
  return message.get('tenant')

  