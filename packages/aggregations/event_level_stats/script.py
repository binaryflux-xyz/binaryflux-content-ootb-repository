def type() :
    return 'event_level_stats'

def columns() : #column names to be aggregated
    return ['event_level']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('event_level')