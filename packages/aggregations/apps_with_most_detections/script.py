def type() :
    return 'apps_detection_map'

def columns() : #column names to be aggregated
    return ['applicationname']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('applicationname')