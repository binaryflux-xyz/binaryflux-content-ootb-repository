def type() :
    return 'entity_app_frequency_map'

def columns() : #column names to be aggregated
    return ['source_ip' , 'applicationname']

def archive() :
    return 'monthly'

def uniquekey(message):
  return message.get('source_ip')+'_'+message.get('applicationname')