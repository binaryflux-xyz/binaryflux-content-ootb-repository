def type() :
    return 'account_detection_map'

def columns() : #column names to be aggregated
    return ['source_account_name']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('source_account_name')
  