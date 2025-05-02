def type() :
    return 'event_type_stats'

def columns() : #column names to be aggregated
    return ['event_type']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('event_type')