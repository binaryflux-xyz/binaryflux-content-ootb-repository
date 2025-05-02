def type() :
    return 'top_user_name'

def columns() : #column names to be aggregated
    return ['user_name']

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('user_name')