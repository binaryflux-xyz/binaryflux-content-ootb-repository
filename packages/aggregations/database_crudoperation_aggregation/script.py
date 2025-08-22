def type() :
    return 'database_crud_data'

def columns() : #column names to be aggregated
    return ['user_name','operation']

def archive() :
    return 'monthly'

def uniquekey(message):
    return None
    