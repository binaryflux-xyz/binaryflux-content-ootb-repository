def type() :
    return 'database_top_user'

def columns() : #column names to be aggregated
    return ['user_name']

def archive() :
    return 'monthly'

def uniquekey(message):
  return None

  