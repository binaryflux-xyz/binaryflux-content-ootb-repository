def type() :
    return 'entity_app_frequency_map'

def columns() : #column names to be aggregated
    return ['source_ip' , 'applicationname']

def archive() :
    return 'monthly'

def uniquekey(message):
  try:
    return message.get('source_ip')+'_'+message.get('applicationname')
  except:
     return None