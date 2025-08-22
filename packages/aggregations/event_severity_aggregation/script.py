def type() :
    return 'event_severity_message'

def columns() : #column names to be aggregated
    return ['user_name','event_severity','dbname','message']

def archive() :
    return 'monthly'

def uniquekey(message):
    return None
    