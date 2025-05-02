def type() :
    return 'top_category_name'

def columns() : #column names to be aggregated
    return ['category_name','category_source']

def archive() :
    return 'monthly'

def uniquekey(message):
  try:
    return message.get('category_name')+'_'+message.get('category_source')
  except:
     return None