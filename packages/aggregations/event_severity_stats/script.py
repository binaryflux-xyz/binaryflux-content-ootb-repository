def type() :
    return 'event_severity_stats'

def columns() : #column names to be aggregated
    return ['event_severity']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('event_severity')