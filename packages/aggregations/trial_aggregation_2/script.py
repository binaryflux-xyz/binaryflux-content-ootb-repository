def type() :
    return 'trialstats2'

def columns() : #column names to be aggregated
    return ['user.domain']

def archive() :
    return 'daily'

def uniquekey(message):
  return message.get('user.domain')

  