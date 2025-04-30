def type() :
    return 'country_detection_map'

def columns() : #column names to be aggregated
    return ['destination_country']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('destination_country')