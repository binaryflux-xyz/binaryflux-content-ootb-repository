def type() :
    return 'eventstat_data'

def columns() : #column names to be aggregated
    return ['event_description']

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('event_description')