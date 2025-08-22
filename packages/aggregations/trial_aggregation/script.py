def type() :
    return 'trialstats'

def columns() : #column names to be aggregated
    return ['user.domain' , 'cloud.provider' ]

def archive() :
    return 'daily'

def uniquekey(message):
  return message.get('user.domain')+"_"+message.get('cloud.provider')