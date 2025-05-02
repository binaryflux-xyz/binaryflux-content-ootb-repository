def type() :
    return 'top_group_name'

def columns() : #column names to be aggregated
    return ['group_name']

def archive() :
    return 'monthly'

def uniquekey(message):
    return message.get('group_name')