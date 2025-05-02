def type() :
    return 'tenant_health_monitor_breakdown'


def columns() : #column names to be aggregated
    return ['tenant','provider','host']

def archive() :
    return 'weekly'

def uniquekey(message):
  return message.get('tenant')