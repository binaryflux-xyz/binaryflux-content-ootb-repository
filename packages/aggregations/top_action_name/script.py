def type() :
    return 'top_action_name'

def columns() : #column names to be aggregated
    return ['event_outcome']

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('event_outcome')