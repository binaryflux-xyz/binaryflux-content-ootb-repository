def type() :
    return 'top_event_details'

def columns() : #column names to be aggregated
    return ['event_description','kaspersky_event_category','kaspersky_event_entity','kaspersky_event_action']

def archive() :
    return 'monthly'

def uniquekey(message):
  try:
    return message.get('event_description')+'_'+message.get('kaspersky_event_category')+'_'+message.get('kaspersky_event_entity')
  except:
     return None