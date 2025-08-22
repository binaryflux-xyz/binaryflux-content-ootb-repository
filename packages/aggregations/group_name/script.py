
def type() :
    return 'top_group_name'

def columns() : #column names to be aggregated
    return ['group_name']

def archive() :
    return 'monthly'

def uniquekey(message):
    try:
        return "im in message"
    except:
        return None
        